class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def dp(i):
            if i >= n:
                return i == n
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dp(i + 1) + dp(i + 2)

            return memo[i]
        
        return dp(0)

"""
Intuition: Every step is based on the one before and the one two before. The base case is the steps where
there are no previous ones to take in which case you return something like 1. You keep doing this until
you get to the end.
"""