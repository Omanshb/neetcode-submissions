class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, hold):
            if i >= len(prices):
                return 0
            
            if (i, hold) in memo:
                return memo[(i, hold)]
            
            memo[(i, hold)] = 0
            if hold:
                memo[(i, hold)] = max(prices[i] + dp(i + 2, False), dp(i + 1, True))
            else:
                memo[(i, hold)] = max(-prices[i] + dp(i + 1, True), dp(i + 1, False))
            

            return memo[(i, hold)]
        
        return dp(0, False)
