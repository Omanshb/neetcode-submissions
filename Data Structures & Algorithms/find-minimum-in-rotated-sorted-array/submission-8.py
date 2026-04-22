class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right and nums[left] > nums[right]:
            middle = (left + right) // 2

            if nums[left] > nums[right]:
                if nums[middle] < nums[right]:
                    right = middle
                else:
                    left = middle + 1
        return nums[left]