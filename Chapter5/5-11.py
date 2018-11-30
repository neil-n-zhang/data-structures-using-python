#cocktail sort
def cocktail_sort(nums):
    for i in range(len(nums)-1,0,-1):
        swap_time=0
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j + 1]=nums[j+1],nums[j]
                swap_time+=1
        if swap_time==0:
            break
        swap_time = 0
        for k in range(j,0,-1):
            if nums[k] < nums[k-1]:
                nums[k], nums[k-1] = nums[k-1], nums[k]
                swap_time += 1
        if swap_time == 0:
            break


a=[2,3,4,5,1]
cocktail_sort(a)

a=[1,2,3,4,5]
cocktail_sort(a)

a=[5,4,3,2,1]
cocktail_sort(a)