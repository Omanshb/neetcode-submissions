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
