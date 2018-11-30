import operator

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

class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def buildparsetree(equation):
    tokenlist=equation.split()
    tree_ancestor=Stack()
    tree=BinaryTree('')
    tree.insertleft('')
    tree_ancestor.push(tree)
    currenttree=tree.getleftchild()

    for token in tokenlist:
        if token=='(':
            tree_ancestor.push(currenttree)
            currenttree.insertleft('')
            currenttree=currenttree.getleftchild()
        elif token in '+-*/':
            tree_ancestor.push(currenttree)
            currenttree.setrootval(token)
            currenttree.insertright('')
            currenttree=currenttree.getrightchild()
        elif token!=')':
            currenttree.setrootval(token)
            currenttree=tree_ancestor.pop()
        elif token==')':
            currenttree=tree_ancestor.pop()
        else:
            raise ValueError('Unkown operator:' + token)
    return tree


def evaluate_tree(parsetree):
    left=parsetree.getleftchild()
    right=parsetree.getrightchild()
    if left==None and right==None:
        return float(parsetree.getrootval())
    else:
        opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
        fn=opers[parsetree.getrootval()]
        return fn(evaluate_tree(left),evaluate_tree(right))

a=buildparsetree('3 + 5')


a=buildparsetree('( 3 + 5 ) * 2')
a.getrootval()
a.getrightchild().getrootval()
a.getleftchild().getrootval()
a.getleftchild().getleftchild().getrootval()
a.getleftchild().getrightchild().getrootval()

evaluate_tree(a)

a=buildparsetree('( ( 3 + 5 ) * 2)')