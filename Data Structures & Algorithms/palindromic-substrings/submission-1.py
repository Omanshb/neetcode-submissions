class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(l, r):
            count = 0
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

            return count
        
        ans = 0
        for i in range(len(s)):
            ans += check(i, i)
            ans += check(i, i + 1)

        return ans