class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        def helper(index):
            if index == len(nums):
                ans.append(cur[:])
                return
            
            cur.append(nums[index])
            helper(index + 1)
            cur.pop()
            helper(index + 1)

            return
        helper(0)
        return ans