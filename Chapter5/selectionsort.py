def selectionsort(nums):
    for end in range(len(nums)-1,0,-1):
        maxpos=0
        for index in range(1,end+1):
            if nums[index]>nums[maxpos]:
                maxpos=index
        nums[end],nums[maxpos]=nums[maxpos],nums[end]



a=[1,4,2,3,5,7,8,6]
selectionsort(a)