class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mnp = prices[0]
        for p in prices:
            if p < mnp:
                mnp = p
            else:
                ans = max(ans, p - mnp)

        return ans