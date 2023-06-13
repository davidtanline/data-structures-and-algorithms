'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List

def two_sum(nums: List[int], target: int) :
        numbers = {}
        for index in range(len(nums)):
            if ((target - nums[index]) in numbers.keys()):
                return [numbers[target-nums[index]], index]
            else:
                numbers[nums[index]] = index

        return [0,0]

# tests
print("Case 1 --- Expected: [0, 1], Actual: ", two_sum([2,7,11,15], 9))
print("Case 2 --- Expected: [1, 2], Actual: ", two_sum([3,2,4], 6))
print("Case 1 --- Expected: [0, 1], Actual: ", two_sum([3,3], 6))
