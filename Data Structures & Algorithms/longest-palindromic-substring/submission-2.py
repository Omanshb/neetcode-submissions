class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            ms = ""
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                ms = s[l: r + 1]
                l -= 1
                r += 1

            return ms
        
        ans = ""
        for i in range(len(s)):
            odd = check(i, i)
            even = check(i, i + 1)

            if len(odd) > len(ans):
                ans = odd
            
            if len(even) > len(ans):
                ans = even
        
        return ans
                