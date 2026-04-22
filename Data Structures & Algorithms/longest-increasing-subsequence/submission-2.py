class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        ans = 0
        for i in range(len(dp)):
            mx = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    mx = max(mx, dp[j])
            dp[i] = 1 + mx
            ans = max(ans, dp[i])
        return ans
