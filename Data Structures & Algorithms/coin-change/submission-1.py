class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            mn = float('inf')
            for coin in coins:
                if i - coin < 0:
                    continue
                mn = min(mn, dp[i - coin] + 1)
            dp[i] = mn
        return dp[-1] if dp[-1] != float('inf') else -1