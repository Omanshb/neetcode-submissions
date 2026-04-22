class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def helper(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            skip = helper(i + 1, buying)
            if buying:
                buy = helper(i + 1, not buying) - prices[i]
                cache[(i, buying)] = max(buy, skip)
            else:
                sell = helper(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(skip, sell)
            return cache[(i, buying)]
        return helper(0, True)