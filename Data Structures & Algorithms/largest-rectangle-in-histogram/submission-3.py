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

"""
Intuition: For every single height in the histogram, the amount largest rectangle that
we can make with that being the height is 
(HEIGHT * (DISTANCE UNTIL SHORTER ON THE RIGHT - DISTANCE UNTIL SHORTER ON THE LEFT)).

For example, in [7,1,7,2,2,4], for the 7 on h[2], there is no space on the left or the
right since both are smaller. For this reason, the rectangle would just have size 7. 
However, with something like the 2 on h[3], there is 1 spot on the left (7) and 2 spots
on the right (2, 4), so the maximum rectangle would be (2 * (4)) or 8.

In order to calculate this, we must use a stack. Before we add to the stack, we keep
popping from it as long as the stack top height is less than the current one. This is
because for all of those heights, we have found the "right limit" and they can be popped
and calculated. As we do this, we update the "left limit" for the current height.

Finally, at the end, we also calculate the max rectangle for the things left in the stack.

Time Complexity: O(n) time because at any given height, we're doing constant operations.

Space Complexity: O(n) becaus we're just maintainiing a stack with the heights.
"""