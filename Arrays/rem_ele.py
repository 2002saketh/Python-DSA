def rem_ele(arr,tar):
    write=0

    for read in range(len(arr)):
        if arr[read]!=tar:
            arr[write]=arr[read]
            write+=1
    return arr[:write]
print(rem_ele([1,2,2,2,3,3,4],2))