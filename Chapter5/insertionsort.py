def insertionsort(nums):
    for end_pos in range(len(nums)-1):
        current_num=nums[end_pos+1]
        pos=end_pos
        while pos>=0 and nums[pos]>current_num:
            nums[pos+1]=nums[pos]
            pos-=1
        nums[pos+1]=current_num


a=[3,1,5,7,2,0,10]
insertionsort(a)