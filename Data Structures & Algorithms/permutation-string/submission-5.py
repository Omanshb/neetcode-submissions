class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        p = 0
        ref = [0] * 26
        tracker = [0] * 26

        for c in s1:
            ref[ord(c) - ord('a')] += 1

        for c in s2:
            index = ord(c) - ord('a')
            tracker[index] += 1
            while tracker[index] > ref[index]:
                tracker[ord(s2[p]) - ord('a')] -=1
                p += 1
    
            
            if ref == tracker:
                return True
        
        return False