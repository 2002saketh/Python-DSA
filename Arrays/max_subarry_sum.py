def max_subarray_sum(arr):
    maxs=arr[0]
    currs=arr[0]

    for i in range(1,len(arr)):
        currs=max(arr[i],arr[i]+currs)
        maxs=max(maxs,currs)
    return maxs
print(max_subarray_sum([1,2,3,-7,2,1]))