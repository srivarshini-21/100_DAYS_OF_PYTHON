from turtle import Turtle
ALIGNMENT = "center"
FONT = ("monotype corsiva",18,"bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score} ",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} ",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align="center",font=("garamond",50,"bold"))


        