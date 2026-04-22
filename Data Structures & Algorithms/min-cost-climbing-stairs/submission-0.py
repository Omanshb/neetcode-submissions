class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost.copy() + [0]

        for i in range(2, len(dp)):
            dp[i] = dp[i] + min(dp[i - 1], dp[i - 2])
        
        return dp[-1]