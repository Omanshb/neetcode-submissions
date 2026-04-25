class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dp(c1, c2, c3):
            if c3 >= len(s3):
                return c2 == len(s2) and c1 == len(s1)
            
            if (c1, c2, c3) in memo:
                return memo[(c1, c2, c3)]
            
            memo[(c1, c2, c3)] = False

            if c1 < len(s1) and s1[c1] == s3[c3]:
                memo[(c1, c2, c3)] = dp(c1 + 1, c2, c3 + 1)
            
            if c2 < len(s2) and s2[c2] == s3[c3]:
                memo[(c1, c2, c3)] = memo[(c1, c2, c3)] or dp(c1, c2 + 1, c3 + 1)
            
            return memo[(c1, c2, c3)]
        
        return dp(0, 0, 0)

                