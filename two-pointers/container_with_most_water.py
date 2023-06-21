'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

from typing import List

def max_area(height: List[int]) -> int:
    maximumArea, l , r = 0, 0, len(height) - 1
    while l < r:
        area = (r - l) * (min(height[r], height[l]))
        maximumArea = max(maximumArea, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maximumArea

# tests
print("Case 1 --- Expected: 49, Actual: ", max_area([1,8,6,2,5,4,8,3,7]))
print("Case 2 --- Expected: 1, Actual: ", max_area([1,1]))

