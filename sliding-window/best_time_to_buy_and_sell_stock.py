'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

from typing import List

def max_profit(prices: List[int]) -> int:
    maximum, minimum = 0, prices[0]
    for price in prices:
        maximum = max(maximum, price - minimum)
        minimum = min(minimum, price)
    return maximum

# tests
print("Case 1 --- Expected: 5, Actual: ", max_profit([7,1,5,3,6,4]))
print("Case 2 --- Expected: 0, Actual: ", max_profit([7,6,4,3,1]))
