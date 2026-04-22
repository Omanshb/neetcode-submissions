class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        mx = 0

        while p1 < p2:
            mx = max(mx, min(heights[p1], heights[p2]) * (p2 - p1))

            if heights[p1] <= heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return mx

"""
Intuition: We start with p1 marking the left bar and p2 marking the right bar. At any point, the calculation
for the amount of water the container can store is min(heights[p1], heights[p2]) * (p2 - p1). Then, as we're
going through the array, we move whichever height between p1 or p2 is lower since that's the limiting factor
and the only way we can possibly store more water. For example, if heights[p1] is 2 and heights[p2] is 5,
no matter how much we move p2, the highest amount of water we can store is still 2. At every step, calculate
the amount of water and update max. At the end, just update max.

Time Complexity: O(n) since the calculation of the water is O(1) and we just iterate through the array.
Space Complexity: O(1) since we don't store anything else in an array other than the original heights 
which is provided.
"""