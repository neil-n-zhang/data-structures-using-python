import timeit
import random

for i in range(10000,100001,20000):
    num=random.randrange(i)
    t=timeit.Timer("num in x","from __main__ import num,x")
    x=list(range(i))
    timelist=t.timeit(1000)

    x={j:None for j in range(i)}
    timedic=t.timeit(1000)
    print("Time for %d list is %f, dic is %f"%(i,timelist,timedic))