class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightPref = [1]
        leftPref = [1]
        for i in range(len(nums)):
            leftPref.append(leftPref[-1] * nums[i])
            rightPref.append(rightPref[-1] * nums[len(nums) - 1 - i])
        rightPref = rightPref[::-1]

        ans = []
        for i in range(len(nums)):
            ans.append(leftPref[i] * rightPref[i + 1])
        return ans