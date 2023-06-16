'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

def is_anagram(s: str, t: str):
        if (len(s) != len(t)):
            return False
        letters = [0] * 26
        for letter in s:
            letters[ord(letter) - ord('a')] += 1
        for letter in t:
            if letters[ord(letter) - ord('a')] == 0:
                return False
            else:
                letters[ord(letter) - ord('a')] -= 1
        return True


# tests
print("Case 1 --- Expected: True, Actual: ", is_anagram("anagram", "nagaram"))
print("Case 2 --- Expected: False, Actual: ", is_anagram("rat", "car"))
print("Case 3 --- Expected: True, Actual: ", is_anagram("racecar", "carrace"))