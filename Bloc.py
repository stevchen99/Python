""" auteur: Thierry Massart
   date : 9 avril 2018
   but du programme : trace avec turtle les contours d’un pavé hexagonal
"""
import turtle

i = 0
for i in range(3):  # à chaque itération, trace un losange
   angle = 120

   if i == 0 :
       turtle.fillcolor("red")
   elif i == 1:
        turtle.fillcolor("black")
   else :
       turtle.fillcolor("blue")

   turtle.begin_fill()
   for j in range(4): # à chaque itération, trace un segment
       turtle.forward(20)
       turtle.left(angle)
       angle = 180 - angle

   turtle.end_fill()
   turtle.right(120)

   turtle.hideturtle()

