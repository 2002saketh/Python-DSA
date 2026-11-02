def two_sum_sorted(arr,tar):
    left=0
    right=len(arr)-1
    while left<right:
        total=arr[left]+arr[right]
        
        if total==tar:
            return [left,right]
        elif total<target:
            left+=1 
        else:
            right-=1 
    return -1
print(two_sum_sorted([1,2,3,4,5],6))