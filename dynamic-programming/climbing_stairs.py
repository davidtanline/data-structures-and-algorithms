'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


def climb_stairs(n: int):
    memo = {}
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2] if n > 1 else 1


# tests
print("Case 1 --- Expected: 1, Actual:", climb_stairs(1))
print("Case 2 --- Expected: 3, Actual:", climb_stairs(3))
print("Case 3 --- Expected: 21, Actual:", climb_stairs(7))
