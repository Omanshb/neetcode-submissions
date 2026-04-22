class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            if nums[l] > nums[r]:
                if nums[middle] > nums[r]:
                    l = middle + 1
                else:
                    r = middle
            else:
                r = l
        
        return nums[l]


        