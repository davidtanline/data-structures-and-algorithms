'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''


def check_inclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map, s2Map, matches = [0] * 26, [0] * 26, 0

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Map[i] == s2Map[i]: matches += 1

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            s2Map[ord(s2[r]) - ord('a')] += 1
            if s1Map[ord(s2[r]) - ord('a')] == s2Map[ord(s2[r]) - ord('a')]:
                matches += 1
            elif s1Map[ord(s2[r]) - ord('a')] + 1 == s2Map[ord(s2[r]) - ord('a')]:
                matches -= 1

            s2Map[ord(s2[l]) - ord('a')] -= 1
            if s1Map[ord(s2[l]) - ord('a')] == s2Map[ord(s2[l]) - ord('a')]:
                matches += 1
            elif s1Map[ord(s2[l]) - ord('a')] - 1 == s2Map[ord(s2[l]) - ord('a')]:
                matches -= 1

            l += 1

        return matches == 26

# tests
print("Case 1 --- Expected: True, Actual: ", check_inclusion("ab", "eidbaooo"))
print("Case 2 --- Expected: False, Actual: ", check_inclusion("ab", "eidboaoo"))