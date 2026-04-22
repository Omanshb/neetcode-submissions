class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        mxProfit = 0
        for price in prices[1:]:
            mxProfit = max(mxProfit, price - minPrice)
            if price < minPrice:
                minPrice = price
        return mxProfit