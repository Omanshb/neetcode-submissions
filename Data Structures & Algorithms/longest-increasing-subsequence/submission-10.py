class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i):
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = 1
            for x in range(i + 1, len(nums)):
                if nums[x] > nums[i]:
                    memo[i] = max(memo[i], dp(x) + 1)
            
            return memo[i]
        
        return max(dp(i) for i in range(len(nums)))