class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        p = 0

        ans = 0

        for i in range(len(s)):
            if s[i] in track:
                while s[i] in track:
                    track.remove(s[p])
                    p += 1
            track.add(s[i])
            ans = max(ans, i - p + 1)

        return ans

        