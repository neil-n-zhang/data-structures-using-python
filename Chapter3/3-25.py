from sys import path
path.append('D:\Data_structure\Chapter3')
from unorderedlist import UnorderedList,Node
import timeit

mylist=UnorderedList()
syslist=[]


popmy = timeit.Timer("mylist.add(0)", "from __main__ import mylist")
print("Time for mylist is",popmy.timeit(number=1000))

popsys=timeit.Timer("syslist.append(0)","from __main__ import syslist")
print("Time for syslist is",popsys.timeit(number=1000))
