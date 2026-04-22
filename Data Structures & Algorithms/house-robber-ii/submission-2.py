class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dp(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            skip = dp(i + 1, flag)
            rob = dp(i + 2, flag) + nums[i]

            memo[i][flag] = max(skip, rob)

            return memo[i][flag]

        
        return max(dp(0, True), dp(1, False))