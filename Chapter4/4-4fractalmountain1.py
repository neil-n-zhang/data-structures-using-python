from turtle import *
import random
#http://grahamsprojects.blogspot.com/2014/08/creating-2d-fractal-landscape-generator.html
class Line:
    def __init__(self):
        self.left=[]
        self.middle=[]
        self.right=[]

def drawTriangle(line1,line2,line3,color,myturtle):
    myturtle.up()
    myturtle.goto(line1.left)
    myturtle.down()
    myturtle.fillcolor(color)
    myturtle.begin_fill()
    myturtle.goto(line1.right)
    myturtle.goto(line3.right)
    myturtle.goto(line2.right)
    myturtle.end_fill()

def midpoint(point1,point2,roughness):
    x=(point1[0]+point2[0])/2+random.uniform(-roughness,roughness)
    y = (point1[1] + point2[1]) / 2+random.uniform(-roughness,roughness)
    return (x,y)

def sierpinski(line1,line2,line3,degree,roughness,myturtle,mywin):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    if degree==1:
        drawTriangle(line1,line2,line3, colormap[degree], myturtle)
        return
    #if degree==2:

    else:
        #mywin.clear()
        if line1.middle==[]:
            line1.middle=midpoint(line1.left,line1.right,roughness)
        if line2.middle==[]:
            line2.middle=midpoint(line2.left,line2.right,roughness)
        if line3.middle==[]:
            line3.middle=midpoint(line3.left,line3.right,roughness)

        line_a=Line()
        line_a.left=line1.left
        line_a.right=line1.middle
        line_b = Line()
        line_b.left = line2.middle
        line_b.right = line2.right
        line_c = Line()
        line_c.left = line1.middle
        line_c.right = line2.middle
        line_d = Line()
        line_d.left = line1.middle
        line_d.right = line1.right
        line_e = Line()
        line_e.left = line3.middle
        line_e.right = line1.middle
        line_f = Line()
        line_f.left = line3.left
        line_f.right = line3.middle
        line_g = Line()
        line_g.left = line2.middle
        line_g.right = line3.middle
        line_h = Line()
        line_h.left = line2.left
        line_h.right = line2.middle
        line_i = Line()
        line_i.left = line3.middle
        line_i.right = line3.right


        sierpinski(line_a,line_b,line_c,degree-1,roughness,myturtle,mywin)
        sierpinski(line_d,line_e,line_f,degree-1,roughness,myturtle,mywin)
        sierpinski(line_g,line_h,line_i, degree - 1, roughness,myturtle,mywin)
        sierpinski(line_g,line_c,line_e, degree - 1, roughness, myturtle, mywin)

#test
myTurtle = Turtle()
myWin = myTurtle.getscreen()
myTurtle.speed(2000)
line1=Line()
line2=Line()
line3=Line()
myPoints = [[-200,-100],[0,200],[200,-100]]
line1.left=myPoints[1]
line1.right=myPoints[0]
line2.left=myPoints[2]
line2.right=myPoints[1]
line3.left=myPoints[0]
line3.right=myPoints[2]
sierpinski(line1,line2,line3,4,5,myTurtle,myWin)
myWin.exitonclick()



