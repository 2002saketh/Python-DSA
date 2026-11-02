def container(heights):
    left,right=0,len(heights)-1
    max_area=0
    while left<right:
        width=right-left
        height=min(heights[left],heights[right])
        area=width*height

        max_area=max(area,max_area)

        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return max_area
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(container(heights))