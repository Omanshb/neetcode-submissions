import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        nums = [-x for x in nums]

        heap = []
        for i in range(k):
            heapq.heappush(heap, (nums[i], i))

        ans = []
        for i in range(k, len(nums) + 1):
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            
            ans.append(-heap[0][0])

            if i < len(nums):
                heapq.heappush(heap, (nums[i], i))
        
        return ans
            
