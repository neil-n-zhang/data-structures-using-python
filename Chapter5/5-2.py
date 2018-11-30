import timeit

def binarysearch_ite(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


def binarysearch_rec(lists,item):

    if len(lists)==0:
        return False
    else:
        middle=int(len(lists)/2)
        if lists[middle]==item:
            return True
        else:
            if lists[middle]>item:
                return binarysearch_rec(lists[:middle], item)
            else:
                return binarysearch_rec(lists[middle+1:], item)

#test the performance
ite = timeit.Timer("binarysearch_ite([2,3,4,5,6,7],5)", "from __main__ import binarysearch_ite")
print("Time for iteration", ite.timeit(number=1000))

rec=timeit.Timer("binarysearch_rec([2,3,4,5,6,7],5)","from __main__ import binarysearch_rec")
print("Time for recursive is",rec.timeit(number=1000))


#recursive function is faster, maybe calculating start,end takes extra time