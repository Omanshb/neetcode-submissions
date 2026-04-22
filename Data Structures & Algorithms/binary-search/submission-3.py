class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle + 1
        
        return -1