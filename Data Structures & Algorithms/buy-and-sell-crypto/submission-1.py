class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mnPrice = prices[0]
        mxProfit = 0
        for price in prices:
            mnPrice = min(price, mnPrice)
            mxProfit = max(mxProfit, price - mnPrice)
        return mxProfit