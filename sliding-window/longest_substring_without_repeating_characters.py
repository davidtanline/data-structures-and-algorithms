'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''

def length_of_longest_substring(s: str) -> int:
    l, r, n, res = 0, 0, len(s), 0
    letters = {}

    while r < n:
        if s[r] in letters.keys() and letters[s[r]] >= l:
            l = letters[s[r]] + 1
        letters[s[r]] = r
        r += 1
        res = max(res, r - l)
    
    return res

# tests
print("Case 1 --- Expected: 3, Actual: ", length_of_longest_substring("abcabcbb"))
print("Case 2 --- Expected: 1, Actual: ", length_of_longest_substring("bbbbb"))
print("Case 3 --- Expected: 3, Actual: ", length_of_longest_substring("pwwkew"))


