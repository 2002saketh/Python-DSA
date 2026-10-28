def max_product_subarray(nums):
    max_product=nums[0]
    gmax=nums[0]
    gmin=nums[0]
    for i in nums:
        if i<0:
            gmax,gmin=gmin,gmax
        gmax=max(i,i*gmax)
        gmin=min(i,i*gmin)

        max_product=max(gmax,max_product)
    return max_product
print(max_product_subarray([1,2,-4,3,2]))