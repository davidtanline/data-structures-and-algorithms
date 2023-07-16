'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def is_valid(s: str) -> bool:
    stack = []
    hm = {")": "(", "]": "[", "}":"{"}
    for ch in s:
        if ch in hm: # character is closing bracket
            if not stack or stack.pop() != hm[ch]: # stack is empty or brackets don't match
                return False
        else: # add to stack if open bracket
            stack.append(ch)
    return True if not stack else False

# tests
print("Case 1 --- Expected: True, Actual: ", is_valid("()"))
print("Case 2 --- Expected: True, Actual: ", is_valid("()[]([])"))
print("Case 3 --- Expected: False, Actual: ", is_valid("(]"))