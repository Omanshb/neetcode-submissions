class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = (len(s) + 1) * [False]
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) >= len(dp):
                    continue
                if s[i: i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]
