def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([5, 3, 2, 1]))     # False