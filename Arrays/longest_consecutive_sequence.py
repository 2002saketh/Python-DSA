def longest_consecutive(nums):
    num_set=set(nums)
    longest=0
    for i in nums:
        if i-1 not in num_set:
            current=i 
            length=1

            while current+1 in num_set:
                current+=1
                length+=1
            longest=max(longest,length)
    return longest
print(longest_consecutive([1,2,8,9,4,3,77]))
