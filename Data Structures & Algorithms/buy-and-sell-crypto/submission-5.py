class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        ans = 0
        for i in range(len(prices) - 1, -1, -1):
            mx = max(mx, prices[i])
            ans = max(ans, mx - prices[i])
        
        return ans

"""
Intuition: Iterate over the list, either forward or backwards. Keep track of the highest number you've seen
after this specific point. Then, at every iteration, you want to take that max and subtract from the current
to get the optimal profit for if you "bought" at this time and "sold" at the max. Keep track of which value
gives us the highest value for this across the array and just return it.

Time Complexity: O(n) since we're just iterating over the list backwards once
Space Complexity: O(1) since we just have to store mx and ans as variables and nothing else
"""