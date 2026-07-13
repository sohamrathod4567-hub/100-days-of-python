# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.shapesize(5)
# timmy.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("name",["Pikchu","Raichu","poplichu","Saapwalapokemon" ])
table.add_column("Type",["Bijliwala","Uparwalejesa","idk","hm" ])
table.align = "l"

print(table)