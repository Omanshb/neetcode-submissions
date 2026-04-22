class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i):
            if i > amount:
                return float('inf')
            
            if i == amount:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = min([dp(i + c) for c in coins]) + 1

            return memo[i]
        
        ans = dp(0)
        
        return ans if ans != float('inf') else -1