class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(i):
            if i >= len(s):
                print(i)
                return True
            
            if i in memo:
                return memo[i]
            
            memo[i] = False
            for word in wordDict:
                if len(word) > len(s[i:]):
                    continue

                if word == s[i:i + len(word)] and dp(i + len(word)):
                    memo[i] = True
                    break
            
            return memo[i]
        
        return dp(0)
