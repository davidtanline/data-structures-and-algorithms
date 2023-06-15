'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [None] * n
    prefix[0] = 1
    res = [None] * n
    cur = 1
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 1, -1, -1):
        res[i] = prefix[i] * cur
        cur *= nums[i]
    return res

# tests
print("Case 1 --- Expected: [24, 12, 8, 6], Actual: ", product_except_self([1,2,3,4]))
print("Case 2 --- Expected: [0, 0, 9, 0, 0], Actual: ", product_except_self([-1,1,0,-3,3]))
