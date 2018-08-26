
x = list(range(2000000))


import timeit
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
print("Time for popzero is",popzero.timeit(number=1000))

poplast=timeit.Timer("x.pop()","from __main__ import x")
print("Time for poplast is",poplast.timeit(number=1000))

for i in [2000000,20000000]:
    x=list(range(i))
    popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    print("Time for popzero %d is" %i, popzero.timeit(number=100))

    poplast=timeit.Timer("x.pop()","from __main__ import x")
    print("Time for poplast %d is" %i, poplast.timeit(number=100))