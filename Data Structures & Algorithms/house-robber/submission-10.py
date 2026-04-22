class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i):
            if i not in range(len(nums)):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            skip = dp(i + 1)
            rob = dp(i + 2) + nums[i]

            memo[i] = max(skip, rob)
            return memo[i]
        
        return dp(0)