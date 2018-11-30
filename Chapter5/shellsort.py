def shellsort(nums):
    sublist_len=len(nums)//2
    while sublist_len>=1:
        for start in range(sublist_len):
            gapinsertionsort(nums,start,sublist_len)
            print(sublist_len,nums)
        sublist_len=sublist_len//2

def gapinsertionsort(nums,start,sublist_len):
    for end_pos in range(start,len(nums)-sublist_len,sublist_len):
        current_num=nums[end_pos+sublist_len]
        pos=end_pos
        while pos >= start and nums[pos] > current_num:
            nums[pos + sublist_len ]=nums[pos]
            pos-=sublist_len
        nums[pos + sublist_len]=current_num

a=[1,5,7,2,3,4,0,3]
shellsort(a)