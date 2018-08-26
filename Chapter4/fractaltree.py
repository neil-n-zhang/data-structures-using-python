import turtle

def tree(myTurtle,length):
    if length>5:
        myTurtle.forward(length)
        myTurtle.right(20)
        tree(myTurtle,length-15)
        myTurtle.left(40)
        tree(myTurtle,length-15)
        myTurtle.right(20)
        myTurtle.backward(length)

myTurtle=turtle.Turtle()
tree(myTurtle,110)
myWin=myTurtle.getscreen()
myWin.exitonclick()