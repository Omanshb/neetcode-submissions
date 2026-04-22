class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def helper(pick):
            if len(curr) == len(nums):
                ans.append(curr.copy())
            
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True

                    curr.append(nums[i])
                    helper(pick)
                    curr.pop()

                    pick[i] = False

        helper([False] * len(nums))

        return ans
