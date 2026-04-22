class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []

        def isPali(st, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def helper(i):
            # if we've made it to the end, just add the whole array to ans
            if i >= len(s):
                ans.append(curr.copy())
                return
            
            # Check all of the next sets that are valid palindromes to add them
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    curr.append(s[i : j + 1])
                    helper(j + 1)
                    curr.pop()
        
        helper(0)
        return ans
            