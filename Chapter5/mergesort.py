def mergesort(nums):
    midpoint=len(nums)//2
    leftnums=nums[:midpoint]
    rightnums=nums[midpoint:]

    if len(nums) > 1:
        mergesort(leftnums)
        mergesort(rightnums)

    i=0
    j=0
    k=0
    while i<len(leftnums) and j<len(rightnums):
        if leftnums[i]<rightnums[j]:
            nums[k]=leftnums[i]
            i+=1
            k+=1
        else:
            nums[k]=rightnums[j]
            j+=1
            k+=1
    while i<len(leftnums):
        nums[k] = leftnums[i]
        i += 1
        k += 1
    while j<len(rightnums):
        nums[k] = rightnums[j]
        j += 1
        k += 1


a=[3,1,5,7,2,0,10]
mergesort(a)