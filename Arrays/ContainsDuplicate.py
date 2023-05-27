"""
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
"""


from typing import List


def contains_duplicate(nums:List[int]):
    # store elements into dictionary, if element already in dictionary return true
    dict = {}
    for i in nums:
        if i in dict:
            return True
        dict[i] = 1
    return False

# tests
print("Case 1 --- Expected: True, Actual: ", contains_duplicate([1,2,3,1]))
print("Case 2 --- Expected: False, Actual: ", contains_duplicate([1,2,3,4]))
print("Case 3 --- Expected: True, Actual: ", contains_duplicate([1,1,1,3,3,4,3,2,4,2]))