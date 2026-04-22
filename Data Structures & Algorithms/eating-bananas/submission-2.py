class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            middle = (l + r) // 2
            sm = sum([-(p // -middle) for p in piles])
            if sm > h:
                l = middle + 1
            elif sm <= h:
                r = middle
        
        return l
        

        