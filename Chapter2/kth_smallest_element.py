#https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
import random
#QuickSelect
def quickselect(nums,k):
    num_choice=random.choices(nums)[0]
    nums_copy=nums.copy()
    nums_copy.remove(num_choice)
    small=[]
    large=[]
    for i in nums_copy:
        if i<=num_choice:
            small.append(i)
        else:
            large.append(i)
    if len(small)==k-1:
        print(num_choice)
        return
    elif len(small)<k-1:
        large.append(num_choice)
        quickselect(large,k-len(small))
    else:
        small.append(num_choice)
        quickselect(small,k)


a=[7, 10, 4, 3, 20, 15]
k=5
quickselect(a,k)
