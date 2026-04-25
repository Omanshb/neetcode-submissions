class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, val):
            if i >= len(nums):
                return int(val == target)
            
            if (i, val) in memo:
                return memo[(i, val)]
            
            memo[(i, val)] = dp(i + 1, val + nums[i]) + dp(i + 1, val - nums[i])
            return memo[(i, val)]
        
        return dp(0, 0)
