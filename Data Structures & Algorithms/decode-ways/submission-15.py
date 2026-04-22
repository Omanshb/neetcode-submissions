class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)

        def dp(i):
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            ways = dp(i + 1)
            
            if i + 1 in range(len(s)) and int(s[i: i + 2]) < 27:
                ways += dp(i + 2)
            
            memo[i] = ways
            return memo[i]
        
        return dp(0)