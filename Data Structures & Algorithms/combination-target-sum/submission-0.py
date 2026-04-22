class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def helper(i, sm):
            if sm >= target:
                if sm == target:
                    ans.append(cur[:])
                return
            if i >= len(nums):
                return
            
            cur.append(nums[i])
            helper(i, sm + nums[i])
            cur.pop()
            helper(i + 1, sm)
        helper(0, 0)
        return ans