'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

import math


def valid_palindrome(s:str):
    # remove all non-alphanumeric characters
    alnumS = ''.join(filter(str.isalnum, s))
    # convert all letters to lowercase
    alnumS = alnumS.lower()
    for i in range(math.ceil(len(alnumS) / 2)):
        if (alnumS[i] is not alnumS[len(alnumS) - i - 1]):
            return False
    return True


# tests
print("Case 1 --- Expected: True, Actual: ", valid_palindrome('A man, a plan, a canal: Panama'))
print("Case 2 --- Expected: False, Actual: ", valid_palindrome('race a car'))
print("Case 3 --- Expected: True, Actual: ", valid_palindrome(' '))