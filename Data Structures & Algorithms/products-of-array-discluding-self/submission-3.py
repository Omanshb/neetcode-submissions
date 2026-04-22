class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix1 = []
        prod = 1
        for n in nums:
            prod *= n
            prefix1.append(prod)
        
        prefix2 = []
        prod = 1
        for n in nums[::-1]:
            print(n)
            prod *= n
            prefix2.append(prod)
        
        prefix2 = prefix2[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(prefix2[i + 1])
            elif i == len(nums) - 1:
                ans.append(prefix1[i - 1])
            else:
                ans.append(prefix1[i - 1] * prefix2[i + 1])

        return ans