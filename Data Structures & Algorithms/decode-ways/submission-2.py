class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = (len(s) + 1) * [0]
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            sm = dp[i + 1]

            if i + 1 < len(s):
                if s[i + 1] == '0' and int(s[i:i+2]) > 26:
                    return 0
                if s[i] != "0" and int(s[i:i+2]) <= 26:
                    sm += dp[i + 2]
            dp[i] = sm
        return dp[0]

