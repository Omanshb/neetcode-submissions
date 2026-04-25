class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
    
        memo = {}

        def dp(i, left):
            if left <= 0:
                return left == 0
            
            if (i, left) in memo:
                return memo[(i, left)]
            

            for x in range(i + 1, len(nums)):
                memo[(i, left)] = dp(i + 1, left - nums[i]) or dp(i + 1, left)
                if memo[(i, left)]:
                    return True

            memo[(i, left)] = False
            return False
        
        return dp(0, target)
