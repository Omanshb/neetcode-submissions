class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        strack = dict()
        ttrack = dict()

        for c in s:
            strack[c] = strack.get(c, 0) + 1
        
        for c in t:
            ttrack[c] = ttrack.get(c, 0) + 1
        
        for key in strack.keys():
            if ttrack.get(key, 0) != strack.get(key):
                return False
        return True

        