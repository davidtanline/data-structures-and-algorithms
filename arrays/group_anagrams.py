'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
        answer = []
        
        # have a dictionary in which each anagram is a key
        anagrams = {}

        for word in strs:
            list_word = list(word) # word as a list
            list_word.sort() # sort the list
            sorted_word = ''.join(list_word) # word is now sorted
            if sorted_word in anagrams: # if key in dict
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        for a in anagrams:
            answer.append(anagrams[a])
        
        return answer

# tests
print("Case 1 --- Expected: [['bat'],['nat','tan'],['ate','eat','tea']], Actual: ", group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print("Case 2 --- Expected: [['']], Actual: ", group_anagrams([""]))
print("Case 3 --- Expected: [['a']], Actual: ", group_anagrams(["a"]))