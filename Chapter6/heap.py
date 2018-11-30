class Heap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0

    def percup(self,i):
        while i>0:
            if self.heaplist[i//2]>self.heaplist[i]:
                self.heaplist[i // 2],self.heaplist[i]=self.heaplist[i],self.heaplist[i//2]
            i=i//2

    def insert(self,num):
        self.heaplist.append(num)
        self.currentsize+=1
        self.percup(self.currentsize)

    def minchild(self,i):
        if 2*i+1>self.currentsize:
            return 2*i
        else:
            if self.heaplist[2*i]<self.heaplist[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def percdown(self,i):
        while i*2<=self.currentsize:
            mc_order=self.minchild(i)
            if self.heaplist[i]>self.heaplist[mc_order]:
                self.heaplist[i],self.heaplist[mc_order]=self.heaplist[mc_order],self.heaplist[i]
                i=mc_order
            else:
                break

    def delmin(self):
        min_num=self.heaplist[1]
        self.heaplist[1]=self.heaplist.pop()
        self.currentsize-=1
        self.percdown(self.heaplist[1])
        return min_num

    def buildheap(self,alist):
        self.heaplist=[0]+alist
        self.currentsize=len(alist)
        i=self.currentsize//2
        while i>0:
            self.percdown(i)
            i-=1

a=Heap()
a.insert(2)
a.insert(1)
a.insert(4)
a.heaplist

a=Heap()
a.buildheap([0, 27, 9,11, 14, 18, 19, 21, 33, 17])
a.percdown(1)

