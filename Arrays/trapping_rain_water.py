def trap_rain_water(heights):
    left=0
    right=len(heights)-1

    lmax=0
    rmax=0

    water=0
    while left<right:
        if heights[left]<=heights[right]:
            lmax=max(heights[left],lmax)
            water+=lmax-heights[left]
            left+=1
        else:
            rmax=max(heights[right],rmax)
            water+=rmax-heights[right]
            right-=1
    return water
heights = [4, 2, 0, 3, 2, 5]
print(trap_rain_water(heights))
