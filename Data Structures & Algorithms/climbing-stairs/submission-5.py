class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]

"""
Intuition: Every step is based on the one before and the one two before. The base case is the steps where
there are no previous ones to take in which case you return something like 1. You keep doing this until
you get to the end.
"""