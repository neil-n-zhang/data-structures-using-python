class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

import random
class Printer():
    def __init__(self,ppm):
        self.printrate=ppm
        self.remainingtime=0

    def addtask(self,task):
        page=task.getpage()
        self.remainingtime=page/self.printrate*60

    def print(self):
        if self.remainingtime>0:
            self.remainingtime-=1

class Task():
    def __init__(self,time):
        self.page=0
        self.timestamp=time

    def getpage(self):
        self.page=random.randrange(1,21)
        return self.page

def newtask():
    if random.randrange(1,181)==180:
        return True
    else:
        return False

def simulation(time,ppm):
    printer1=Printer(ppm)
    taskQueue=Queue()
    waittime=[]

    for i in range(time):
        if newtask():
            task=Task(i)
            taskQueue.enqueue(task)
        if printer1.remainingtime>0:
            printer1.print()
        else:
            if taskQueue.size()>0:
                task1=taskQueue.dequeue()
                printer1.addtask(task1)
                waittime1=i-task1.timestamp
                waittime.append(waittime1)
    print("Average wainting time is %6.2f secs %3d tasks remaining."%(sum(waittime)/len(waittime),taskQueue.size()))


for i in range(10):
    simulation(3600,10)
