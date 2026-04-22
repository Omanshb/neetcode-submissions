class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        memo = [-1] * len(s)

        def dp(i):
            if i >= len(s):
                return 1
                
            if s[i] == '0':
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            ways = 0
            
            if i + 1 in range(len(s)):
                if int(s[i: i + 2]) < 27:
                    ways = dp(i + 2) + dp(i + 1)
                else:
                    ways = dp(i + 1)
            else:
                ways = dp(i + 1)
            
            memo[i] = ways
            return memo[i]
        
        return dp(0)