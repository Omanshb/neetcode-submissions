class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        # Keep track of current sum and index being handled
        def helper(sm, i):
            # If sum exceeds target prune this branch
            if sm > target:
                return 
            
            # if no more indexes left, check if it's == target 
            if i >= len(nums):
                if sm == target:
                    ans.append(curr.copy())
                return
            
            # We can stay in this spot and add this index
            curr.append(nums[i])
            helper(sm + nums[i], i)
            curr.pop()

            # we can go to the next spot
            helper(sm, i + 1)
        
        helper(0, 0)

        return ans