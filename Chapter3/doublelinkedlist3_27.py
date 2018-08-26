class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
        self.before=None

    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def getbefore(self):
        return self.before

    def setdata(self,newdata):
        self.data=newdata
    def setnext(self,newnext):
        self.next=newnext
    def setbefore(self,newnext):
        self.before=newnext

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.end=None
    def isempty(self):
        return self.head==None
    def addhead(self,newdata):
        temp=Node(newdata)
        temp.setnext(self.head)
        if self.head==None:
            self.head=temp
            self.end=temp
        else:
            self.head.setbefore(temp)
            self.head=temp
    def addend(self,newdata):
        temp=Node(newdata)
        temp.setbefore(self.end)
        if self.end==None:
            self.head=temp
            self.end=temp
        else:
            self.end.setbefore(temp)
            self.end=temp
    def length(self):
        size=0
        node=self.head
        while node!=None:
            size+=1
            node=node.getnext()
        return size
    def search(self,target):
        found=False
        current=self.head
        while current!=None and found==False:
            if current.getdata()==target:
                found=True
            current=current.getnext()
        return found
    def remove(self,target):
        found = False
        current = self.head
        previous=None
        while current != None and found == False:
            if current.getdata() == target:
                if previous!=None:
                    previous.setnext(current.getnext())
                else:
                    self.head=current.getnext()
                found = True
            else:
                previous=current
                current = current.getnext()
        return found

#test
mylist=DoubleLinkedList()
mylist.addhead(31)
mylist.addhead(11)
mylist.addhead(21)
mylist.addhead(4)
mylist.addhead(54)
mylist.remove(31)
mylist.remove(11)
mylist.search(31)

