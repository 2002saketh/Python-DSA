def move_neg_nos(arr):
    left=0
    right=len(arr)-1
    while left<right:
        while left<right and arr[left]<0:
            left+=1
        while left<right and arr[right]>=0:
            right-=1

        if left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return arr
print(move_neg_nos([1,-1,2,-2,3,-3,-4,5]))