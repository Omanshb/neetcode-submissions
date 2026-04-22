class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1

        mx = min(heights[p1], heights[p2]) * (p2 - p1)
        while p1 < p2:
            while p1 < p2 and heights[p1] <= heights[p2]:
                p1 += 1
                mx = max(mx, min(heights[p1], heights[p2]) * (p2 - p1))

            
            while p1 < p2 and heights[p2] < heights[p1]:
                p2 -= 1
                mx = max(mx, min(heights[p1], heights[p2]) * (p2 - p1))
        
        return mx
                
        