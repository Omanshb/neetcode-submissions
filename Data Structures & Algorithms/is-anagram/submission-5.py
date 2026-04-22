class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        strack = dict()
        ttrack = dict()

        for i in range(len(s)):
            strack[s[i]] = strack.get(s[i], 0) + 1
            ttrack[t[i]] = ttrack.get(t[i], 0) + 1

        
        for key in strack.keys():
            if ttrack.get(key, 0) != strack.get(key):
                return False
        return True

        