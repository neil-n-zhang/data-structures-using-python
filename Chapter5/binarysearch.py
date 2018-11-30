def binarysearch(lists,item):
    found=False
    start=0
    end=len(lists)-1
    while start<=end and not found:
        middle=int((start+end)/2)
        if lists[middle]==item:
            found=True
        else:
            if lists[middle]>item:
                end=middle-1
            else:
                start=middle+1
    return found

binarysearch([2,3,4,5,6,7],5)