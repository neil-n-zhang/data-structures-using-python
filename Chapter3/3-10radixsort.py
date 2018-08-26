#https://www.geeksforgeeks.org/radix-sort/
#假设有n个数字，有m个桶，如果数字是平均分布的，则每个桶里面平均有n / m个数字。如果对每个桶中的数字采用快速排序，那么整个算法的复杂度是O(n + nlogn - nlogm)
#从上式看出，当m接近n的时候，桶排序复杂度接近O(n),以上复杂度的计算是基于输入的n个数字是平均分布这个假设的。
import math
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

def radixsort(numbers):
    mainbin=Queue()
    maxdigit=math.ceil(math.log10(max(numbers)))
    for num in numbers:
        mainbin.enqueue(num)
    digitbin=[]
    for i in range(10):
        digitbin.append(Queue())
    for i in range(maxdigit):
        for j in range(mainbin.size()):
            number=mainbin.dequeue()
            remainder=number//10**i%10
            digitbin[remainder].enqueue(number)
        for j in range(10):
            for k in range(digitbin[j].size()):
                mainbin.enqueue(digitbin[j].dequeue())
    for i in range(mainbin.size()):
        print(mainbin.dequeue())
    return