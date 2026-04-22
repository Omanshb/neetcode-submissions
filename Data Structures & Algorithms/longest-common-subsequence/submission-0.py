class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text1) for i in range(len(text2))]
        for i in range(len(text1)):
            dp[0][i] = max(dp[0][i-1], 1 if text2[0] == text1[i] else 0)
        for i in range(len(text2)):
            dp[i][0] = max(dp[i-1][0], 1 if text1[0] == text2[i] else 0)
        
        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]