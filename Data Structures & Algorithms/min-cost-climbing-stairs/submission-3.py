class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memoize the repeated recursive calls
        memo = [-1] * len(cost)

        # recursion function
        def dp(i):
            # if we have reached the top, just return 0 (we don't have any step cost here)
            if i >= len(cost):
                return 0
            
            # if memo[i] has a value, we don't have to do the repeated recursion and can return here
            if memo[i] != -1:
                return memo[i]
            
            # calculate memo[i] by checking minimum of next two steps and adding the current cost as well
            memo[i] = min(dp(i + 1), dp(i + 2)) + cost[i]
            return memo[i]
        
        # return the minimum of starting from the first or second step
        return min(dp(0), dp(1))