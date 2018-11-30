import timeit

def binarysearch_recindex(lists,start,end,item):
    if start<end:
        return False
    else:
        middle=int(len(lists)/2)
        if lists[middle]==item:
            return True
        else:
            if lists[middle]>item:
                return binarysearch_recindex(lists,start,middle-1, item)
            else:
                return binarysearch_recindex(lists,middle+1,end, item)

def binarysearch_recslice(lists,item):
    if len(lists)==0:
        return False
    else:
        middle=int(len(lists)/2)
        if lists[middle]==item:
            return True
        else:
            if lists[middle]>item:
                return binarysearch_recslice(lists[:middle], item)
            else:
                return binarysearch_recslice(lists[middle+1:], item)

#test the performance
recindex = timeit.Timer("binarysearch_recindex([2,3,4,5,6,7],0,5,5)", "from __main__ import binarysearch_recindex")
print("Time for recursive index is", recindex.timeit(number=1000))

recslice=timeit.Timer("binarysearch_recslice([2,3,4,5,6,7],5)","from __main__ import binarysearch_recslice")
print("Time for recursive slice is",recslice.timeit(number=1000))


#recursive function is faster, maybe calculating start,end takes extra time