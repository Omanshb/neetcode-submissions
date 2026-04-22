class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            tracker = {}
            for j in range(len(nums)):
                if j == i:
                    continue
                if target - nums[j] in tracker:
                    ans.add(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                tracker[nums[j]] = j
        return [list(x) for x in ans]