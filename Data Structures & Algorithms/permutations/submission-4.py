class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []


        def helper(pick):
            # if curr has the same length as nums, we can just add it to ans
            if len(curr) == len(nums):
                ans.append(curr.copy())
            
            # we want to consider every single number that hasn't been picked yet
            for i in range(len(nums)):
                if not pick[i]:

                    # pick it, then move to the next recursion, and then unpick it
                    pick[i] = True

                    curr.append(nums[i])
                    helper(pick)
                    curr.pop()

                    pick[i] = False

        # start with a pick list that's fully False
        helper([False] * len(nums))

        return ans
