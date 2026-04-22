import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue
            
            else:
                heapq.heappush(stones, -abs(stone1 - stone2))
        
        return -stones[0] if stones else 0