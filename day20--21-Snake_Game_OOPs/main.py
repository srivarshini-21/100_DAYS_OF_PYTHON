from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food)<20: # Considering the food is 10 x 10 circle we cannot check '==0' condition because that means the snake head has to touch the centre of the circle food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: # -300 < -290 = Wall hit
        game_on=False
        scoreboard.game_over()

    # # Detect collision with tail
    # for segment in snake.segments:
    #     if segment==snake.head:
    #         pass
    #     elif snake.head.distance(segment)<10:
    #         game_on=False
    #         scoreboard.game_over()

    # Detect collision with tail using slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()






screen.exitonclick()