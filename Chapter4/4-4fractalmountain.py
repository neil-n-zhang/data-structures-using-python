from turtle import *
import random
#http://grahamsprojects.blogspot.com/2014/08/creating-2d-fractal-landscape-generator.html
class Line:
    def __init__(self):
        self.left=[]
        self.middle=[]
        self.right=[]

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

def midpoint(point1,point2,roughness):
    x=(point1[0]+point2[0])/2+random.uniform(-roughness,roughness)
    y = (point1[1] + point2[1]) / 2+random.uniform(-roughness,roughness)
    return (x,y)

def sierpinski(points,degree,roughness,myturtle,mywin):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    if degree==1:
        drawTriangle(points, colormap[degree], myturtle)
        return
    #if degree==2:

    else:
        #mywin.clear()
        midpoint1=midpoint(points[0],points[1],roughness)
        midpoint2 = midpoint(points[0], points[2], roughness)
        midpoint3= midpoint(points[1], points[2], roughness)
        sierpinski([points[0],midpoint1,midpoint2],degree-1,roughness,myturtle,mywin)
        sierpinski([midpoint1, points[1], midpoint3],degree-1,roughness,myturtle,mywin)
        sierpinski([midpoint2, midpoint3,points[2]], degree - 1, roughness,myturtle,mywin)
        sierpinski([midpoint1,midpoint2, midpoint3], degree - 1, roughness, myturtle, mywin)

#test
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [[-200,-100],[0,200],[200,-100]]
sierpinski(myPoints,3,5,myTurtle,myWin)
myWin.exitonclick()

