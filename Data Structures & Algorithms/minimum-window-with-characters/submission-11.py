class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = {}
        for c in t:
            ref[c] = ref.get(c, 0) + 1
        
        p = 0
        track = {}
        extra = {}
        ans = ""
        for i in range(len(s)):
            track[s[i]] = track.get(s[i], 0) + 1
            if track[s[i]] > ref.get(s[i], 0):
                extra[s[i]] = track[s[i]] - ref.get(s[i], 0)
            
            while p < i and extra.get(s[p], 0) != 0:
                track[s[p]] = track.get(s[p], 0) - 1
                extra[s[p]] = extra.get(s[p], 0) - 1
                p += 1
            
            contains = True
            for key, value in ref.items():
                if track.get(key, 0) < value:
                    contains = False

            
            if contains:
                if not ans or len(ans) > i - p + 1:
                    ans = s[p:i+1]
    
        return ans
        
        
                
                
                
