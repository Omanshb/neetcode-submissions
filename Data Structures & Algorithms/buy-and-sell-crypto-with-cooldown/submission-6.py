class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, coin):
            if i >= len(prices):
                return 0
            
            if (i, coin) in memo:
                return memo[(i, coin)]
            
            memo[(i, coin)] = 0
            if coin >= 0:
                memo[(i, coin)] = max(memo[(i, coin)], dp(i + 2, -1) + prices[i] - prices[coin], dp(i + 1, coin))
            else:
                memo[(i, coin)] = max(memo[(i, coin)], dp(i + 1, i), dp(i + 1, -1))

            return memo[(i, coin)]
        
        return dp(0, -1)
