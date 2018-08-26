#http://blog.christianperone.com/2015/08/googles-s2-geometry-on-the-sphere-cells-and-hilbert-curve/
#http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html

from turtle import *
def hilbert(x,y,xx,xy,yx,yy,n,myturtule):
    if n==0:
        if x==y==0:
            myturtle.up()
            myturtle.goto([x+(xx+yx)/2,y+(xy+yy)/2])
            myturtle.down()
        else:
            myturtule.goto([x+(xx+yx)/2,y+(xy+yy)/2])
    else:
        hilbert(x,              y,              yx/2,       yy/2,       xx/2,       xy/2,   n-1, myturtule)
        hilbert(x+xx/2,         y+xy/2,         xx / 2,     xy / 2,     yx / 2,     yy / 2, n - 1, myturtule)
        hilbert(x + xx/2+yx/2,  y+xy/2+yy/2,    xx / 2,     xy / 2,     yx / 2,     yy / 2, n - 1, myturtule)
        hilbert(x + xx/2+yx,    y + xy/2+yy,    -yx/2,      -yy / 2,    -xx / 2,    -xy / 2, n - 1, myturtule)

myturtle = Turtle()
hilbert(0,0,200,0,0,200,4,myturtle)
myWin = myturtle.getscreen()
myWin.exitonclick()