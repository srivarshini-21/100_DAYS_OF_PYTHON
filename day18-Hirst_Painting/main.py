# import colorgram
# colors=colorgram.extract('image.jpeg',64)
# colors_list=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_list.append((r,g,b))
# print(colors_list)
import turtle as t
import random

t.colormode(255)
tom=t.Turtle()

colors_list=[(244, 229, 50), (202, 7, 33), (237, 228, 2), (193, 67, 24), (221, 151, 81), (36, 210, 91), (240, 41, 122), (35, 92, 177), (32, 31, 156), (205, 11, 5), (16, 18, 53), (92, 185, 218), (64, 9, 44), (231, 156, 6), (58, 21, 10), (206, 31, 94), (219, 134, 178), (12, 201, 221), (18, 149, 28), (90, 237, 168), (237, 58, 31), (81, 212, 150), (96, 75, 9), (238, 160, 199), (87, 87, 206), (6, 37, 28), (10, 96, 62), (90, 227, 239), (239, 170, 161), (253, 6, 21), (254, 7, 5), (174, 178, 226), (3, 247, 219), (12, 57, 249), (0, 249, 253)] # Copy the list printed in console and delete the tuples which are shades of white and then comment out the colorgram code
tom.hideturtle()
tom.speed(0)
tom.setheading(225)
tom.penup()
tom.forward(300)
tom.setheading(0)
tom.pendown()
rows=0
while rows<10:
    for _ in range(10):
        color=random.choice(colors_list)
        tom.dot(20, color)
        tom.penup()
        tom.forward(50)

    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(500)
    tom.right(180)
    rows+=1

screen=t.Screen()
screen.exitonclick()
