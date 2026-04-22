class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]
        maxRight = [0]

        for i in range(len(height)):
            maxLeft.append(max(maxLeft[-1], height[i]))
            maxRight.append(max(maxRight[-1], height[len(height) - 1 - i]))
        
        maxRight = maxRight[::-1]

        print(maxLeft, maxRight)

        total = 0

        for i in range(len(height)):
            total += max(min(maxLeft[i], maxRight[i + 1]) - height[i], 0)
        
        return total

"""
Intuition: The hardest part about this problem is figuring out how much water to add at any given point.
However, after going through several test cases, it's quite obvious. At any given point, you look at the
tallest elevation that has been seen on the left and the tallest elevation that has been seen on the right.
You know that the limiting factor is always the lower elevation of those two. So that's max height which the
water is being stored to. Then, you have to also account for your current elevation so you subtract your current
height from that. Since we can have the max height be 0 and the current height be like 2, you have to make sure
that you aren't subtracting from the total at any given time accidentally and are doing max(addition, 0)

Time Complexity: O(n) since it costs linear time to create the two max prefix arrays and linear time to sum up
the total.
Space Complexity: O(n) since we just store the max prefix arrays.
"""