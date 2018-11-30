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

def preorder(tree):
    if tree:
        print(tree.getrootval())
        preorder(tree.getleftchild())
        preorder(tree.getrightchild())

def inorder(tree):
    if tree:
        inorder(tree.getleftchild())
        print(tree.getrootval())
        inorder(tree.getrightchild())

def postorder(tree):
    if tree:
        postorder(tree.getleftchild())
        postorder(tree.getrightchild())
        print(tree.getrootval())


def printexp(tree):
    exp=''
    if tree:
        exp=exp+'('+printexp(tree.getleftchild())
        exp=exp+tree.getrootval()
        exp =exp+printexp(tree.getrightchild())+')'
    return exp