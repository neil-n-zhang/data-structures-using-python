from sys import path
path.append('D:\Data_structure\Chapter3')
from doublelinkedlist3_27 import DoubleLinkedList,Node

import timeit
import random

class Queue(DoubleLinkedList):
    def enqueue(self,newdata):
        super().addhead(newdata)
    def dequeue(self):
        end=self.end
        preceding=end.getbefore()
        if preceding !=None:
            preceding.setnext(None)
        self.end=preceding
        return end.getdata()

#test the performance
for num in [2000,20000]:
    queue_en=Queue()
    queue_de=Queue()
    for i in range(num):
        queue_en.enqueue(random.randrange(num))
        queue_de.enqueue(random.randrange(num))


    addstart = timeit.Timer("queue_en.enqueue(0)", "from __main__ import queue_en")
    print("Time for size %d Queue enqueue is"%num, addstart.timeit(number=1000))

    addend=timeit.Timer("queue_de.dequeue()","from __main__ import queue_de")
    print("Time for size %d Queue dequeue is"%num,addend.timeit(number=1000))


