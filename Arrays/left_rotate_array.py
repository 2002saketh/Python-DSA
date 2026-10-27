def rev(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
def left_rotate(arr,k):
    if len(arr)==0:
        return False
    n=len(arr)
    k=k%n
    rev(arr,0,k-1)
    rev(arr,k,n-1)
    rev(arr,0,n-1)

    return arr
print(left_rotate([1,2,3,4,5],2))