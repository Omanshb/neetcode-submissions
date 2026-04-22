import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = []
        l = 0

        for r in range(len(nums)):
            while d and nums[d[-1]] <= nums[r]:
                d.pop()
            d.append(r)

            while l > d[0]:
                d.popleft()
            
            if r + 1 >= k:
                ans.append(nums[d[0]])
                l += 1
        
        return ans

"""
Intuition: One way to do this problem is to 
"""