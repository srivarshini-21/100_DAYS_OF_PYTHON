from turtle import Turtle
ALIGNMENT = "center"
FONT = ("monotype corsiva",18,"bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        with open(r"day20-21-Snake_Game\data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.goto(0,270)
        self.update_score()
        

    def increase_score(self):
        self.score+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score} ",align=ALIGNMENT,font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open(r"day20-21-Snake_Game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!",align="center",font=("garamond",50,"bold"))


        