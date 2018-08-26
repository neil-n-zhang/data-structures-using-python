import turtle
import random

def tree(myTurtle,length,thickness):
    if length>18:
        myTurtle.color('brown')
    else:
        myTurtle.color('green')
    if length>5:
        myTurtle.pensize(thickness)
        myTurtle.forward(length)
        angle=random.randrange(15,45)
        deltalength=random.randrange(12,17)
        myTurtle.right(angle)
        tree(myTurtle,length-deltalength,thickness-1)
        myTurtle.left(angle*2)
        tree(myTurtle,length-deltalength,thickness-1)
        myTurtle.right(angle)
        myTurtle.up()
        myTurtle.backward(length)
        myTurtle.down()

myTurtle=turtle.Turtle()
myWin=myTurtle.getscreen()
myTurtle.up()
myTurtle.backward(90)
myTurtle.down()
tree(myTurtle,110,8)

myWin.exitonclick()