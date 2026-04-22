class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        picked = [False] * len(nums)
        curr = []


        def helper():
            # if curr has the same length as nums, we can just add it to ans
            if len(curr) == len(nums):
                ans.append(curr.copy())
            
            # we want to consider every single number that hasn't been picked yet
            for i in range(len(nums)):
                if not picked[i]:

                    # pick it, then move to the next recursion, and then unpick it
                    picked[i] = True

                    curr.append(nums[i])
                    helper()
                    curr.pop()

                    picked[i] = False

        # start with a pick list that's fully False
        helper()

        return ans
