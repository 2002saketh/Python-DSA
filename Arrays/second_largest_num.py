def second_largest_number(arr):
    largest=float('-inf')
    slargest=float('-inf')
    for num in arr:
        if num>largest:
            slargest=largest
            largest=num
        elif num>slargest and num!=largest:
            slargest=num
    if slargest==float('-inf'):
        return None
    return slargest
arr=[10,20,4,45,99]
print("Second largest number is:", second_largest_number(arr))