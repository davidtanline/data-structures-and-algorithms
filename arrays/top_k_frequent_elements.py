'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    answer = [] 

    # count how many times a number occurs
    for n in nums:
        count[n] = count.get(n,0) + 1
    
    # group the numbers into their own frequency
    for n, c in count.items():
        freq[c].append(n)

    # go from highest to lowest frequency
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            answer.append(n)
            if len(answer) == k:
                return answer
    
    return answer

# tests
print("Case 1 --- Expected: [1, 2], Actual: ", top_k_frequent([1,1,1,2,2,3], 2))
print("Case 2 --- Expected: [1], Actual: ", top_k_frequent([1], 1))
