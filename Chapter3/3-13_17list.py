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

class UnorderedList:
    def __init__(self):
        self.head=None
        self.length=0
    def __str__(self):
        out='['
        current=self.head
        while current!=None:
            out=out+str(current.getdata())+','
            current=current.getnext()
        if out=='[':
            return '[]'
        else:
            out=out[:-1]+']'
            return out
    def slice(self,start,end):
        out = '['
        current = self.head
        for i in range(start):
            current=current.getnext()
        for i in range(end-start):
            out = out + str(current.getdata()) + ','
            current = current.getnext()
        if out=='[':
            return '[]'
        else:
            out=out[:-1]+']'
            return out
    def isempty(self):
        return self.head==None
    def add(self,newdata):
        temp=Node(newdata)
        temp.setnext(self.head)
        self.head=temp
        self.length+=1
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
        if found:
            self.length-=1
        return found

#test
mylist=UnorderedList()
mylist.add(31)
mylist.add(11)
mylist.add(21)
mylist.add(4)
mylist.add(54)
mylist.remove(31)
mylist.remove(11)
mylist.search(31)