class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        def helper(sm, i):
            if sm > target:
                return 
            
            if i >= len(nums):
                if sm == target:
                    ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(sm + nums[i], i)
            curr.pop()

            helper(sm, i + 1)
        
        helper(0, 0)

        return ans