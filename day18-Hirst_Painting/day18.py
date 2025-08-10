# Explore https://docs.python.org/3/library/turtle.html
from turtle import Turtle,Screen
tommy=Turtle() # Object construction using Turtle class 
print(tommy) # Prints the memory location of the object created
tommy.shape("turtle")
tommy.shapesize(2)
tommy.color("DeepPink4") # Explore colors here - https://cs111.wellesley.edu/labs/lab02/colors
for i in range(0,4): # Draw a square
    tommy.forward(100)
    tommy.right(90)

# Dashed Line
for i in range(0,10):
    tommy.forward(10)
    tommy.penup()
    tommy.forward(10)
    tommy.pendown()
    tommy.forward(10)

# Shapes with random colors
import random
colors=['blue','green yellow','orange','dark violet','dark red','deep pink']
def draw_shape(sides):
    angle=360/sides
    for _ in range(sides):
        tommy.forward(100)
        tommy.right(angle)

for side in range(3,11):
    tommy.pencolor(random.choice(colors))
    draw_shape(side)

# Random Walk
import random
colors=['blue','green yellow','orange','dark violet','dark red','deep pink']
angles=[0,90,270,180]
tommy.pensize(15)
tommy.speed(10)
for i in range(200):
    tommy.pencolor(random.choice(colors))
    tommy.forward(25)
    tommy.setheading(random.choice(angles))

# Generating random colors
import turtle as t
import random
tommy=t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color=(r,g,b)
    return color

tommy.speed(0)

def draw_spiro(gap_size):
    for _ in range(int(360/gap_size)):
        tommy.color(random_color())
        tommy.circle(100)
        current_heading=tommy.heading()
        tommy.setheading(current_heading + 5)

draw_spiro(5)

screen=t.Screen()
screen.exitonclick()