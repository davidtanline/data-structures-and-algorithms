'''
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
'''

import math

def isPerfectSquare(num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            mid = math.floor(l + (r - l) / 2)
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

# tests
print("Case 1 --- Expected: True, Actual: ", isPerfectSquare(16))
print("Case 2 --- Expected: False, Actual: ", isPerfectSquare(14))
print("Case 3 --- Expected: True, Actual: ", isPerfectSquare(1))