def move_zeros(arr):
    write=0
    for read in range(len(arr)):
        if arr[read]!=0:
            arr[read],arr[write]=arr[write],arr[read]
            write+=1
    return arr
print(move_zeros([0,1,0,3,12]))  # Output: [1, 3, 12, 0, 0]