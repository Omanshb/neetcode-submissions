class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = []
        rightProd = []
        currL = 1
        currR = 1
        for i in range(len(nums)):
            currL *= nums[i]
            leftProd.append(currL)

            currR *= nums[len(nums) - 1 - i]
            rightProd.append(currR)
        
        rightProd = rightProd[::-1]

        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(rightProd[i + 1])
            elif i == len(nums) - 1:
                res.append(leftProd[i - 1])
            else:
                res.append(leftProd[i - 1] * rightProd[i + 1])
        
        return res

"""
There is a way to solve this problem where you just hold a prefix array with the total product
so far coming from the left side and another one coming from the right side. Imagine the example
below:

Array -> [5, 2, 9, 4, 6]

prefixLeft -> [5, 10, 90, 360, 2160]
prefixRight -> [2160, 432, 216, 24, 6]

then, say we want to get the product of all but itself for the 3rd value 9, we just do the multiplication
of the left side times the right side so prefixLeft[2] * prefixRight[4] or 10 * 24 = 240.

Time Complexity: O(n) because creating the prefixes and calculating all of the values is linear
Space Complexity: O(n) because prefix arrays and result array are both linear
"""