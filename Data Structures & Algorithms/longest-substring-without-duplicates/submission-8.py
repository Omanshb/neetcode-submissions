class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        p = 0
        ans = 0

        for c in s:
            while c in track:
                track.remove(s[p])
                p += 1
            track.add(c)
            ans = max(ans, len(track))
        
        return ans