# from turtle import Turtle, Screen
#
# turtle = Turtle()
# print(turtle)
# turtle.shape("turtle")
# turtle.color("coral")
# turtle.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# # import prettyTables
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","water","Fire"])
# table.align("l")
print(table)
