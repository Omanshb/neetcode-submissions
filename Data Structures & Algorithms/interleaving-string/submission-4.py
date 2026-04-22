class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def helper(p1, p2):
            if p1 + p2 == len(s3):
                return p1 == len(s1) and p2 == len(s2)
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            
            found = False

            if p1 < len(s1) and s1[p1] == s3[p1 + p2]:
                found = helper(p1 + 1, p2)
            if p2 < len(s2) and s2[p2] == s3[p1 + p2]:
                found = helper(p1, p2 + 1)
            cache[(p1, p2)] = found
            return cache[(p1, p2)]
        return helper(0, 0)