from turtle import *
PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,path):
        self.mazelist=[]
        f=open(path,'r')
        rownum=0
        for line in f:
            colnum=0
            rowlist=[]
            for char in line:
                if char!='\n':
                    rowlist.append(char)
                if char=='S':
                    self.startrow=rownum+1
                    self.startcol=colnum+1
                colnum+=1
            self.mazelist.append(rowlist)
            rownum+=1

        self.totalrow=len(self.mazelist)
        self.totalcol=len(self.mazelist[0])
        self.t=Turtle()
        self.t.shape('turtle')
        self.wn = Screen()
        self.wn.setworldcoordinates(0,-self.totalrow,self.totalcol,0)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for x in range(self.totalcol):
            for y in range(self.totalrow):
                if self.mazelist[y][x]==OBSTACLE:
                    self.drawCenteredBox(x,y,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x,-y)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        self.t.color(color)
        for i in range(4):
            self.t.right(90)
            self.t.forward(1)
        self.t.end_fill()

    def moveTurtle(self,row,col):
        self.t.up()
        self.t.setheading(self.t.towards(col+0.5,-row-0.5))
        self.t.goto(col+0.5,-row-0.5)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col]=val
        self.moveTurtle(row,col)

        if val==PART_OF_PATH:
            color='green'
        elif val==TRIED:
            color='black'
        elif val==DEAD_END:
            color='red'
        else:
            color=None

        if color:
            self.t.dot(color)

    def isExit(self,row,col):
        return (row==0 or col==0 or row==self.totalrow-1 or col==self.totalcol-1)

def searchFrom(maze,row,col):
    maze.updatePosition(row,col)
    if maze.mazelist[row][col]==OBSTACLE or maze.mazelist[row][col]==TRIED or maze.mazelist[row][col]==DEAD_END:
        return False
    if maze.isExit(row,col):
        maze.updatePosition(row,col,PART_OF_PATH)
        return True
    maze.updatePosition(row, col, TRIED)
    found=searchFrom(maze,row-1,col) or searchFrom(maze,row,col-1) or searchFrom(maze,row+1,col) or searchFrom(maze,row,col+1)
    if found:
        maze.updatePosition(row,col,PART_OF_PATH)
    else:
        maze.updatePosition(row, col, DEAD_END)
    return found

a=Maze('D:\Data_structure\Chapter4\maze1.txt')
a.drawMaze()
searchFrom(a,a.startrow-1,a.startcol-1)
