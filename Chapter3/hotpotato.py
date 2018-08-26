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


def hotPotato(namelist,num):
    namequeue=Queue()
    for name in namelist:
        namequeue.enqueue(name)
    while namequeue.size()>1:
        for i in list(range(num)):
            name=namequeue.dequeue()
            namequeue.enqueue(name)
        namequeue.dequeue()
    return namequeue.dequeue()

#test
hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)