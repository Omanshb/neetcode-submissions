class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        
        mx = 0
        for n in s:
            if n - 1 in s:
                continue
            else:
                count = 1
                while n + count in s:
                    count += 1
                mx = max(count, mx)

        return mx