'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''

def min_window(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    
    minLength, minimum = 100001, ""

    # dict (letter, frequency)
    unique = {}
    for letter in t:
        unique[letter] = unique.get(letter, 0) + 1

    l, matches, sMap = 0, 0, {}
    for r in range(len(s)):
        curr = s[r]
        if curr in unique:
            sMap[curr] = sMap.get(curr, 0) + 1
            if sMap[curr] == unique[curr]: matches += 1
        while matches == len(unique):
            if (r - l + 1) < minLength: 
                minimum = s[l:r+1]
                minLength = r - l + 1
            curr = s[l]
            if curr in unique:
                sMap[curr] -= 1
                if sMap[curr] + 1 == unique[curr]: matches -= 1
            l += 1
    
    return minimum

# tests
print("Case 1 --- Expected: \"BANC\", Actual: ", min_window("ADOBECODEBANC", "ABC"))
print("Case 2 --- Expected: \"a\", Actual: ", min_window("a", "a"))
print("Case 3 --- Expected: \"\", Actual: ", min_window("a", "aa"))