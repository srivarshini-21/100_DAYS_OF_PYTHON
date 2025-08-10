# OOP 
from turtle import Turtle,Screen
tommy=Turtle() # Object construction using Turtle class 
print(tommy) # Prints the memory location of the object created
tommy.shape("turtle")
tommy.shapesize(2,2,2)
tommy.color("DeepPink4")
tommy.forward(100)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# pip install prettytable inside venv
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Name",['Ruby','Ronnie','Jennie'])
table.add_column("USN",['001','002','003'])
table.add_row(["Rockie",'004'])
table.align='r'
print(table)
