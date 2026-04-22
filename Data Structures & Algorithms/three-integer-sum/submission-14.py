class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums) - 2):
            target = -nums[i]

            tracker = set()
            for j in range(i + 1, len(nums)):
                if target - nums[j] in tracker:
                    ans.add(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                tracker.add(nums[j])
        
        return [x for x in ans]

"""
Intuition: threeSum is essentially the same problem as 2sum but we have to iterate through the array with
one of the pointers completely in place. In the solution above, we iterate through with i. Then, within the
rest of the remaining array, we just perform a simple 2sum using a set. When we add to the answer array, we 
sort first to avoid duplicates. 

Time Complexity: O(n^2) because running twosum is O(n) time and we do that for every elemnt in the list.
Space Complexity: O(n) becuase we have two sets that are tracking the elements in the list.
"""
                
