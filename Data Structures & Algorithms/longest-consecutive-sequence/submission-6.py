class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        mx = 0
        for n in numset:
            if n - 1 not in numset:
                length = 1
                while n + length in numset:
                    length += 1
                mx = max(length, mx)
        return mx