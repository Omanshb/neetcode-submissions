class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(curr, i):
            if i >= len(nums):
                ans.append(curr[::])
                return

            helper(curr[::], i + 1)
            helper(curr[::] + [nums[i]], i + 1)

        helper([], 0)
        return ans
            
