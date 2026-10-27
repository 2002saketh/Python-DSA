def reverse(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
def right_rotate_array(arr,k):
    if len(arr)==0:
        return
    n=len(arr)
    k=k%n

    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    return arr
print(right_rotate_array([1,2,3,4,5],2))