#cannot run in pycharm console, run the whole file or in python command line
import timeit
import random

for i in range(10000,100001,20000):
    num=random.randrange(i)
    t=timeit.Timer("x.index(num)","from __main__ import num,x")
    x=list(range(i))
    timelist=t.timeit(1000)

    print("Time for %d list is %f"%(i,timelist))