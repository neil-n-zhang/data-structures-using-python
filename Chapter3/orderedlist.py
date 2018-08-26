class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getdata(self):
        return self.data
    def getnext(self):
        return self.next

    def setdata(self,newdata):
        self.data=newdata
    def setnext(self,newnext):
        self.next=newnext

class OrderedList:
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head==None
    def add(self,newdata):
        stop = False
        current = self.head
        previous=None
        temp = Node(newdata)
        if current==None:
            self.head=temp
            stop=True
        else:
            while current != None and stop == False:
                if current.getdata() >= newdata:
                    stop=True
                    if previous==None:
                        temp.setnext(self.head)
                        self.head = temp
                    else:
                        temp.setnext(current)
                        previous.setnext(temp)
                previous=current
                current = current.getnext()
        if stop==False:
            previous.setnext(temp)
    def length(self):
        size=0
        node=self.head
        while node!=None:
            size+=1
            node=node.getnext()
        return size
    def search(self,target):
        found=False
        stop=False
        current=self.head
        while current!=None and found==False and stop==False:
            if current.getdata()==target:
                found=True
            if current.getdata()>target:
                stop=True
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
mylist=OrderedList()
mylist.add(31)
mylist.add(11)
mylist.add(4)
mylist.add(54)
mylist.remove(31)
mylist.remove(11)
mylist.search(31)

