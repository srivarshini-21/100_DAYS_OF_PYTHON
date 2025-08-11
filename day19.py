# Etch-A-Sketch
from turtle import Turtle, Screen
tom=Turtle()
screen=Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def move_left():
    tom.left(10)

def move_right():
    tom.right(10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()

screen.listen()
screen.onkey(key="w",fun=move_forward) # Triggers function when space is pressed; No '()' after function name
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()

# Day 19 Project - Turtle race
from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400) # Set custom dimension for screen

bet=screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
colors=["red",'orange','yellow','green','blue','purple']
y_pos = [-100,-50,0,50,100,150]
turtle_list=[]
for turtle_num in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_num])
    new_turtle.penup()
    new_turtle.goto(x= -230,y= y_pos[turtle_num])
    turtle_list.append(new_turtle) # Instances of turtle, each with its own states

if bet:
    is_race_on=True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on=False
            win_color = turtle.pencolor()
            if win_color==bet:
                print(f"You won! The {win_color} turtle is the winner!")
            else:
                print(f"You lost. The {win_color} turtle is the winner.")
        dist=random.randint(0,10)
        turtle.forward(dist)
screen.exitonclick()