from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor() + self.x_move
        new_y=self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1  # Changes the y direction to -10 which moves the ball in opposite direction during the next iteration of while loop during wall collision

    def bounce_x(self):
        self.x_move *= -1  # Changes the x direction to -10 which moves the ball in oppsite x direction during next iteration of while loop during paddle collision
        self.move_speed *= 0.8 # Increase the ball speed by a bit everytime it hits the paddle
    
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
