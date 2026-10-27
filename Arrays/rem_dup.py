def rem_dup(arr):
    write=0
    for read in range(1,len(arr)):
        if arr[read]!=arr[write]:
            write+=1
            arr[write]=arr[read]
            
    return write+1
arr=[1,1,2,2,3,3,4,4,5,6]
k=rem_dup(arr)
print(arr[:k])