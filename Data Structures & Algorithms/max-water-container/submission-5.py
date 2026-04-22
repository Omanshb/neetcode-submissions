class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        mx = (p2 - p1) * min(heights[p1], heights[p2])
        while p1 < p2:
            if heights[p1] <= heights[p2]:
                prev = heights[p1]
                while p1 < p2 and heights[p1] <= prev:
                    p1 += 1
            elif heights[p2] < heights[p1]:
                prev = heights[p2]
                while p1 < p2 and heights[p2] <= prev:
                    p2 -= 1
            if (p2 - p1) * min(heights[p1], heights[p2]) > mx:
                mx = (p2 - p1) * min(heights[p1], heights[p2])
        return mx
                
