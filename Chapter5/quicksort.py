def quicksort(nums):
    quicksorthelper(nums,0,len(nums)-1)

def quicksorthelper(nums,first,last):
    if first<last:
        partition_pos=partition(nums,first,last)
        quicksorthelper(nums,first,partition_pos-1)
        quicksorthelper(nums,partition_pos+1,last)
        return


def partition(nums,first,last):
    pivot=nums[first]
    left_pos=first+1
    right_pos=last
    while left_pos<right_pos:
        while left_pos<last and nums[left_pos]<pivot:
            left_pos+=1
        while right_pos>first and nums[right_pos]>pivot:
            right_pos-=1
        if left_pos<right_pos:
            nums[left_pos],nums[right_pos]=nums[right_pos],nums[left_pos]
    if nums[first]>nums[right_pos]:
        nums[first],nums[right_pos]=nums[right_pos],nums[first]
    return right_pos


a=[3,5,7,2,1,4,0,3]
quicksort(a)

b=[7, 2, 3, 4, 5, 3]
quicksort(b)

c=[1,2,3,4,5]
quicksort(c)

