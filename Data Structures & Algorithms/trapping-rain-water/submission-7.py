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
            print(total)
            total += max(min(maxLeft[i], maxRight[i + 1]) - height[i], 0)
        
        return total