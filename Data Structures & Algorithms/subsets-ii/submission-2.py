class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        nums.sort()
        def helper(i):
            if i >= len(nums):
                ans.append(cur[:])
                return
            
            cur.append(nums[i])
            helper(i + 1)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1)
        helper(0)
    
        return ans