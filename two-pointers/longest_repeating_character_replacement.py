'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 

You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

def character_replacement(s: str, k: int) -> int:

    letters, l, longest = {}, 0, 0

    for r in range(len(s)):
        letters[s[r]] = letters.get(s[r], 0) + 1
        if (r - l + 1) - max(letters.values()) <= k:
            longest = max(longest, r - l + 1)
        else:
            letters[s[l]] -= 1
            l += 1

    return longest

# tests
print("Case 1 --- Expected: 4, Actual: ", character_replacement("ABAB", 2))
print("Case 2 --- Expected: 4, Actual: ", character_replacement("AABABBA", 1))
