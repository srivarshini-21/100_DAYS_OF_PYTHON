from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score=Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top and bottom walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        
    # Detect right paddle misses    
    if ball.xcor() > 380:
        score.l_point() # When right paddle missed point is added to left paddle player
        ball.reset_ball()

    # Detect left paddle misses    
    if ball.xcor() < -380:
        score.r_point() # When left paddle misses point is added to right paddle player
        ball.reset_ball()

    if score.l_score==5 or score.r_score==5:
        game_on=False
screen.exitonclick()