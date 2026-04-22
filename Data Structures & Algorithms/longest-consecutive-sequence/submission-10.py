class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        viewed = set()
        nums = set(nums)
        
        mx = 0
        
        for n in nums:
            counter = 1
            viewed.add(n)
            while n + counter in nums:
                viewed.add(n + counter)
                counter += 1
            
            mx = max(mx, counter)
        
        return mx


        

        