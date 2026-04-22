class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

"""We obviously know that a set can not contain duplicates of a value.
Thus, by converting our nums list to a set, we are getting rid of all duplicates.
If we just compare this value to the value of the original list, we will
be able to confirm if there were any duplicates by checking if the set is
shorter than the original list.

space complexity: O(n) because the set can have at most the length of the original list
time complexity: O(n) (time complexity of making the set)
"""