'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

from typing import List

def longest_consecutive(nums: List[int]) -> int:
    s = set(nums)
    count = 0

    for n in s:
        if n-1 not in s:
            currSum = 1
            while n + currSum in s:
                currSum += 1
            count = max(count, currSum)
    return count

# tests
print("Case 1 --- Expected: 4, Actual: ", longest_consecutive([100,4,200,1,3,2]))
print("Case 2 --- Expected: 9, Actual: ", longest_consecutive([0,3,7,2,5,8,4,6,0,1]))