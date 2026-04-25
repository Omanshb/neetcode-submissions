class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(x, y):
            print(x, y)
            if x == m - 1 and y == n - 1:
                return 1
            
            if x not in range(m) or y not in range(n):
                return 0
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            memo[(x, y)] = dp(x + 1, y) + dp(x, y + 1)
            return memo[(x, y)]
        
        return dp(0, 0)