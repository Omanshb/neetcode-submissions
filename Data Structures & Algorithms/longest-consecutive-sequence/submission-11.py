class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        mx = 0
        
        for n in nums:
            if n - 1 in nums:
                continue
            
            counter = 1
            while n + counter in nums:
                counter += 1
            
            mx = max(mx, counter)
        
        return mx


"""
Intuition: There are two aspects of this problem which we need to optimize. First of all, if we have a
number n, how do we make it so that searching for n + 1 is an O(n) operation. Obviously, we use a set.
Second of all, how do we make sure that we never search repeatedly in the same sequence. For example, 
searching 2, 3, 4, 5, 6 and then later searching 4, 5, 6 for no reason and wasting time complexity. We
need a way so that we only search when it's the beginning of some sequence. The way to check for this is 
if n - 1 exists in the set. Therefor, first we initialize a set with the contents of the nums. Then, for each
"beginning" number, we search until we can't anymore, keeping track of a counter. Finally, we just return
the max counter which we have recorded.

Time Complexity: O(n) because we never search the same number twice.
Space Complexity: O(n) because we just keep the same list but as a set.
"""

        

        