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
                
