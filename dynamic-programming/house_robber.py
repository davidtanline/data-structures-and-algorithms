'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

from typing import List

def rob(nums: List[int]) -> int:
    if (len(nums) == 1):
        return nums[0]
    dp = [0] * (len(nums))
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[len(dp) - 1]

# Tests
print("Case 1 --- Expected: 4, Actual:", rob([1,2,3,1]))
print("Case 2 --- Expected: 12, Actual:", rob([2,7,9,3,1]))