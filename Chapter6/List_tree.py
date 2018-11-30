def BinaryTree(r):
    return [r,[],[]]

def insertleft(root,newbranch):
    org_left=root.pop(1)
    if org_left==None:
        root.insert(1,[newbranch,[],[]])
    else:
        root.insert(1,[newbranch,org_left,[]])

def insertright(root,newbranch):
    org_right=root.pop(2)
    if org_right==None:
        root.insert(2, [newbranch, [], []])
    else:
        root.insert(2, [newbranch,[],org_right])

def getrootval(root):
    return root[0]

def setrootval(root,val):
    root[0]=val

def getleftchild(root):
    return root[1]
def getrightchild(root):
    return root[2]

r=BinaryTree(3)
insertleft(r,4)
insertright(r,5)
getrootval(r)
getleftchild(r)
