class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dp(i, left):
            if left == 0:
                return 1
            
            if i >= len(coins):
                return 0
            
            if (i, left) in memo:
                return memo[(i, left)]
            

            memo[(i, left)] = dp(i + 1, left)
            if left >= coins[i]:
                memo[(i, left)] += dp(i, left - coins[i])
            
            return memo[(i, left)]
        
        return dp(0, amount)