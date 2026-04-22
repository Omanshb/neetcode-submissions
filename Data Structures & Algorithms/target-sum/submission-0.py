class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def helper(i, cur):
            if i >= len(nums):
                return int(cur == target)
            if (i, cur) in cache:
                return cache[(i, cur)]
            
            cache[(i, cur)] = helper(i + 1, cur - nums[i]) + helper(i + 1, cur + nums[i])
            return cache[(i, cur)]
        
        return helper(0, 0)