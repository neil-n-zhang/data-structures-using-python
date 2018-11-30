class BinaryTree:
    def __init__(self,root):
        self.key=root
        self.leftchild=None
        self.rightchild=None

    def insertleft(self,newnode):
        if self.leftchild==None:
            self.leftchild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.insertleft(self.leftchild)
            self.leftchild=t

    def insertright(self,newnode):
        if self.rightchild==None:
            self.rightchild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.insertright(self.rightchild)
            self.rightchild=t

    def getrightchild(self):
        return self.rightchild
    def getleftchild(self):
        return self.leftchild
    def setrootval(self,obj):
        self.key=obj
    def getrootval(self):
        return self.key



#test
r=BinaryTree(3)

r.getrootval()
r.insertright(4)
r.insertright(5)
r.getleftchild()
r.getrightchild()

