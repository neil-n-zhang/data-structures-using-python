def median(nums):
    sort_nums=sorted(nums)
    if len(nums)%2==0:
        return sort_nums[len(nums)//2-1]
    else:
        return sort_nums[len(nums)//2]

def partition(nums,med):
    small=[]
    large=[]
    for num in nums:
        if num<med:
            small.append(num)
        elif num>med:
            large.append(num)
    new_nums=small+[med]+large
    return new_nums,len(small)


def kthsmallest(nums,k):
    group_num=len(nums)//5

    if group_num==0:
        sorted(nums)
        return nums[k-1]

    median_all=[]

    for i in list(range(group_num)):
        median_all.append(median(nums[5*i:5*(i+1)]))
    if len(nums)>5*(i+1):
        median_all.append(median(nums[5*(i+1):]))


    if len(median_all)%2==0:
        medofmed=kthsmallest(median_all,len(median_all)//2-1)
    else:
        medofmed=kthsmallest(median_all,len(median_all)//2)

    new_nums,pos=partition(nums,medofmed)
    if pos+1==k:
        return medofmed
    elif pos+1>k:
        return kthsmallest(new_nums[:pos],k)
    else:
        return kthsmallest(new_nums[pos+1:],k-pos-1)


nums=[1,4,2,3,5,7,6]
k=4
kthsmallest(nums,k)