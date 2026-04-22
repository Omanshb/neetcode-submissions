class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1

"""
Intuition: Just basic binary search. 

Time Complexity: O(log(n))
Space Complexity: O(1)
"""