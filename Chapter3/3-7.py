#implement a queue such that both enqueue and dequeue have O(1) performance on average.
#https://leetcode.com/articles/implement-queue-using-stacks/

class Queue():
    def __init__(self):
        self.endata=[]
        self.dedata=[]

    def enqueue(self,data):
        self.endata.append(data)

    def dequeue(self):
        if self.dedata==[]:
            if self.endata==[]:
                print('Queue is empty.')
                return
            else:
                self.dedata.append(self.endata.pop())
            return self.dedata.pop()

    def getdata(self):
        return self.endata+self.dedata[::-1]


myqueue=Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.dequeue()
myqueue.getdata()