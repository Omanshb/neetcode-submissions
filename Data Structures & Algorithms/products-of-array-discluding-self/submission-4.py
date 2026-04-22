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


        