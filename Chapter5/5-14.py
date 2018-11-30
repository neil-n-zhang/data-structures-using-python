def mergesort(nums,start,end):
    midpoint=(end+start)//2

    if end-start > 0:
        mergesort(nums,start,midpoint)
        mergesort(nums,midpoint+1,end)

    i=start
    j=midpoint+1
    result=[]
    while i<=midpoint and j<=end:
        if nums[i]<nums[j]:
            result.append(nums[i])
            i+=1
        else:
            result.append(nums[j])
            j += 1
    while i<=midpoint:
        result.append(nums[i])
        i += 1

    while j<=end:
        result.append(nums[j])
        j += 1
    nums[start:end+1]=result


a=[3,1,5,7,2,0,10]
mergesort(a,0,6)

b=[3,1,5,7]
mergesort(b,0,3)

c=[2,0,10]
mergesort(c,0,2)