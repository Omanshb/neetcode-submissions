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
Intuition: One way to do this problem is to maintain a heap as we're 
traversing over the entire nums array. Then, once we have done so, just
checking on each step that the index within the heappop is in the range
appropriate for us. However, another way to solve this problem is through
a deque. Essentially, every time we add a new number into the deque, we 
will pop from the end of the deque while it's less than the new number.
What this does is ensure that the largest value within the window at all
times is at the beginning of the deque and all the other values that aren't
necessary can just be popped away. Then, we also pop from the left side all
of the values whose index is too far left and outside our window. Finally,
we just append nums[d[0]] after we have done these window processing steps.

Time Complexity: O(n) because we are just iterating over the array and doing
O(1) operations at each step.

Space Complexity: O(n) because we are just maintaining a single deque which
will never have a size > k.
"""