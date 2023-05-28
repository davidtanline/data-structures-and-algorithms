'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

from typing import List

def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R*C - 1

        # perform binary search
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // C, mid % C
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

# tests
print("Case 1 --- Expected: True, Actual: ", search_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print("Case 2 --- Expected: False, Actual: ", search_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 17))