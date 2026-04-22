class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        ans = 0
        for i in range(len(prices) - 1, -1, -1):
            mx = max(mx, prices[i])
            ans = max(ans, mx - prices[i])
        
        return ans