class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This is the overall answer tracker
        ans = []
        curr = []

        # at all times, curr is the array that we're handling and i is the index we're considering
        def helper(i):
            # if i >= len(nums), no more values to consider and we can return after adding the array
            if i >= len(nums):
                ans.append(curr.copy())
                return

            # two paths possible:
            # 1. skip this index value and then move on to the next
            # 2. add this index value and then move on to the next
            helper(i + 1)

            curr.append(nums[i])
            helper(i + 1)
            curr.pop()

        helper(0)
        return ans
            
