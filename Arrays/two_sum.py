def two_sum(arr,target):
    seen={}
    for i,n in enumerate(arr):
        diff=target-n
        if diff in seen:
            return [seen[diff],i]
        seen[n]=i
    return -1
print(two_sum([1,2,3,4],5))