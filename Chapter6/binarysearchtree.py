class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size

    def put(self,key,val):
        if self.root==None:
            self.root=TreeNode(key,val)
        else:
            self._put(key,val,self.root)
        self.size+=1
    def _put(self,key,val,node):
        if key<node.key:
            if node.hasleftchild():
                self._put(key,val,node.leftchild)
            else:
                node.leftchild=TreeNode(key,val,parent=node)
        else:
            if node.hasrightchild():
                self._put(key,val,node.rightchild)
            else:
                node.rightchild=TreeNode(key,val,parent=node)

    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res==None:
                return res
            else:
                return res.payload
        else:
            return None
    def _get(self,key,node):
        if node==None:
            return None
        elif key==node.key:
            return node
        elif key<node.key:
            return self._get(key,node.leftchild)
        else:
            return self._get(key,node.rightchild)

    def findmin(self,node):
        current=node
        while current.hasleftchild():
            current=current.leftchild
        return current
    def delete(self,key):
        rm_note=self._get(key,self.root)
        if rm_note:
            if self.size==1:
                self.root=None
            else:
                self.remove(rm_note)
        else:
            raise KeyError('Key is not found.')
    def remove(self,rm_note):
        if not rm_note.hasanychild():
            if rm_note.isleftchild():
                rm_note.parent.leftchild=None
            else:
                rm_note.parent.rightchild=None
        if rm_note.hasbothchild():
            succ=self.findmin(rm_note.rightchild)
            self.delete(succ.key)
            rm_note.key=succ.key
            rm_note.payload=succ.payload
        else:
            if rm_note.hasleftchild():
                rm_note.leftchild.parent = rm_note.parent
                if rm_note.isleftchild():
                    rm_note.parent.leftchild=rm_note.leftchild
                else:
                    rm_note.parent.rightchild=rm_note.leftchild
            else:
                rm_note.rightchild.parent = rm_note.parent
                if rm_note.isleftchild():
                    rm_note.parent.leftchild=rm_note.rightchild
                else:
                    rm_note.parent.rightchild=rm_note.rightchild

    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def __setitem__(self, key, value):
        self.put(key,value)
    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right
        self.parent=parent

    def hasleftchild(self):
        return self.leftchild
    def hasrightchild(self):
        return self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild==self
    def isrightchild(self):
        return self.parent and self.parent.rightchild==self

    def isroot(self):
        return not self.parent
    def isleaf(self):
        return not (self.rightchild and self.leftchild)

    def hasanychild(self):
        return self.leftchild or self.rightchild
    def hasbothchild(self):
        return self.leftchild and self.rightchild

    def replacenodedata(self,key,val,left=None,right=None):
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right



tree=BinarySearchTree()
tree.put(17,'a')
tree.put(5,'b')
tree.put(25,'c')
tree.put(2,'d')
tree.put(11,'e')
tree.put(35,'f')
tree.put(9,'g')
tree.put(16,'h')
tree.put(29,'i')
tree.put(38,'j')
tree.put(7,'k')
tree.put(8,'l')

tree.delete(5)
tree.root.leftchild.key
tree.root.leftchild.rightchild.key
tree.root.leftchild.rightchild.leftchild.leftchild.key

tree.get(1)
tree.get(3)
