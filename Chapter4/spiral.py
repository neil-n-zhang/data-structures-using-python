import turtle
myTurtle=turtle.Turtle()
myWin=myTurtle.getscreen()

def drawspiral(myTurtle,length):
    if length>0:
        myTurtle.forward(length)
        myTurtle.right(90)
        drawspiral(myTurtle,length-5)

drawspiral(myTurtle,100)
myWin.exitonclick()