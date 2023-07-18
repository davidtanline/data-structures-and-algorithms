'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    subset = []

    def dfs(i):
        if i == len(nums):
            res.append(subset.copy()) # use copy() to get current value of subset
            return
        # option 1: include current element
        subset.append(nums[i])
        dfs(i+1)

        # option 2: don't include current element
        subset.pop()
        dfs(i+1)
    
    dfs(0)

    return res

# tests
print("Case 1 --- Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], Actual:", subsets([1,2,3]))
print("Case 2 --- Expected: [[],[0]], Actual:", subsets([0]))
