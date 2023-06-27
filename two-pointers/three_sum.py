'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        # end if reach positive numbers
        if a > 0:
            break
        # skip duplicates
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        # for each non positive number, find unique pair(s)
        while l < r:
            tempSum = a + nums[l] + nums[r]
            if tempSum > 0:
                r -= 1
            elif tempSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                while (l < r and nums[r - 1] == nums[r]):
                    r -= 1
                r -= 1
    return res

# tests
print("Case 1 --- Expected: [[-1, -1, 2],[-1, 0, 1]], Actual: ", three_sum([-1,0,1,2,-1,-4]))
print("Case 2 --- Expected: [], Actual: ", three_sum([0,1,1]))
print("Case 3 --- Expected: [[0,0,0]], Actual: ", three_sum([[0,0,0]]))