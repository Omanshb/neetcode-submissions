class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = [0] * 26
        p = 0
        ans = 0
        for i in range(len(s)):
            tracker[ord(s[i]) - ord('A')] += 1
            while max(tracker) + k < i - p + 1:
                tracker[ord(s[p]) - ord('A')] -= 1
                p += 1
            ans = max(ans, i - p + 1)
        return ans