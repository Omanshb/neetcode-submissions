class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        mx = 0

        for i in range(len(heights)):
            ins = (heights[i], i, i)


            while stack and heights[i] <= stack[-1][0]:
                popped = stack.pop()
                mx = max(mx, (i - popped[2]) * popped[0])
                ins = (heights[i], i, popped[2])
        
            stack.append(ins)

        for height, index, start in stack:
            mx = max((len(heights) - start) * height, mx)
        
        return mx
