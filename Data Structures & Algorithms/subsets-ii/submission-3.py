class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def helper(i):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(i + 1)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i = i + 1
            
            helper(i + 1)
        
        nums.sort()
        helper(0)
        return ans