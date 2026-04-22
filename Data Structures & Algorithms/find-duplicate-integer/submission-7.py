class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = nums[0], nums[nums[0]]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        
        return