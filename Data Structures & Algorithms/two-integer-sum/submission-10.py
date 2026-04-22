class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i in range(len(nums)): # O(n)
            if target - nums[i] in tracker:
                return [tracker[target - nums[i]], i]
            tracker[nums[i]] = i
        return [-1, -1]

"""
Intuition: Essentially, for this problem, we go through the array and we keep checking if the difference
between the target and our current number has shown up yet. If it has, we know that the value of that 
number is Target - nums[i] and we just need to return the value of it's index. To keep track of whether
or not that number has occured and then also the index of the occurence, we use a dictionary because a set
is not enough for our needs. As we go through the problem, make sure to keep updating the dictionary
consistently.

Time Complexity: O(n)

Space Complexity: O(n)
"""
