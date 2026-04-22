class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(2, len(nums)):
            target = -nums[i]
            tracker = set()
            for j in range(i):
                if target - nums[j] in tracker:
                        ans.add(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                else:
                    tracker.add(nums[j])
        return list(ans)
