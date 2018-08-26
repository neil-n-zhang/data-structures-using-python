from turtle import *
def drawTriangle(points,color,myturtle):
    myturtle.up()
    myturtle.goto(points[0])
    myturtle.down()
    myturtle.fillcolor(color)
    myturtle.begin_fill()
    myturtle.goto(points[1])
    myturtle.goto(points[2])
    myturtle.goto(points[0])
    myturtle.end_fill()

def midpoint(point1,point2):
    x=(point1[0]+point2[0])/2
    y = (point1[1] + point2[1]) / 2
    return (x,y)

def sierpinski(points,degree,myturtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myturtle)
    if degree>0:
        sierpinski([points[0],midpoint(points[0],points[1]),midpoint(points[0],points[2])],degree-1,myturtle)
        sierpinski([midpoint(points[1], points[0]), points[1], midpoint(points[1], points[2])],degree-1,myturtle)
        sierpinski([midpoint(points[2], points[0]), midpoint(points[1], points[2]),points[2]], degree - 1, myturtle)

#test
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [[-500,-250],[0,500],[500,-250]]
sierpinski(myPoints,6,myTurtle)
myWin.exitonclick()