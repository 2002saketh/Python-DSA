def contains_duplicate(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contains_duplicate([1,2,3,4,5,1]))