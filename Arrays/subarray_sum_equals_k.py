def subarry_sum(arr,k):
    prefix=0
    count=0
    hs={0:1}
    for i in arr:
        prefix+=i
        diff=prefix-k
        if diff in hs:
            count+=hs[diff]
        hs[prefix]=hs.get(prefix,0)+1
    return count
print(subarry_sum([1,2,3],3))