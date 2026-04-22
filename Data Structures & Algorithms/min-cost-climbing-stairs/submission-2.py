class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dp(i):
            if i >= len(cost):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = min(dp(i + 1), dp(i + 2)) + cost[i]
            return memo[i]
        
        return min(dp(0), dp(1))