class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def helper(n):
            if not n:
                ans.append(curr.copy())
            
            for i in range(len(n)):
                new = n.copy()
                new.pop(i)

                curr.append(n[i])
                helper(new)
                curr.pop()
        helper(nums)

        return ans
