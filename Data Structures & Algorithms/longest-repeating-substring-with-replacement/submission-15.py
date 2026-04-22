class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = [0] * 26
        p = 0
        ans = 0
        mx = 0

        for i in range(len(s)):
            tracker[ord(s[i]) - ord('A')] += 1
            mx = max(mx, tracker[ord(s[i]) - ord('A')])

            while mx + k < i - p + 1:
                tracker[ord(s[p]) - ord('A')] -= 1
                p += 1
            
            ans = max(ans, i - p + 1)
        
        return ans
