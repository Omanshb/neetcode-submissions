class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(c1, c2):
            if c1 >= len(text1) or c2 >= len(text2):
                return 0
            
            if (c1, c2) in memo:
                return memo[(c1, c2)]
            
            memo[(c1, c2)] = 0

            if text1[c1] == text2[c2]:
                memo[(c1, c2)] = dp(c1 + 1, c2 + 1) + 1
            
            memo[(c1, c2)] = max(memo[(c1, c2)], dp(c1 + 1, c2), dp(c1, c2 + 1))
            return memo[(c1, c2)]
        
        return dp(0, 0)

            

        