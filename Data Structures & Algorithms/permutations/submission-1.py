class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        def helper():
            if not nums:
                ans.append(cur[:])
                return
            
            for i in range(len(nums)):
                n = nums.pop(0)
                cur.append(n)
                helper()
                cur.pop()
                nums.append(n)
        helper()
        return ans