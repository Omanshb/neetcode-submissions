class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTaken(k):
            ans = 0
            for p in piles:
                ans += -(-p//k)
            return ans
        
        left, right = 1, max(piles)

        while left < right:
            middle = (left + right) // 2
            time = hoursTaken(middle)

            if time > h: 
                left = middle + 1
            elif time <= h:
                right = middle
        
        return left

"""
Intuition: The main issue is that we can't test every single eating speed from 1 to the max(piles). For this reason, we need a faster way
of searching through the possible values and landing on one. This problem really demonstrates how powerful binary search can be when it
comes to fast search and exploring countless options. With this, we're able to see the different eating speeds and ultimately converge
on the smallest one. 

Time Complexity: O(nlog(m)) where n is the length of piles and m is the max number in piles. This is because we perform log(m) searches
and each of those searches takes n time since we have to iterate over the piles array.

Space Complexity: O(1) since there is no added space complexity above the original piles array.
"""
