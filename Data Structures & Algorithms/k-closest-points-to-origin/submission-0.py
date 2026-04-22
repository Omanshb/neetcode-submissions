import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            heapq.heappush(dist, ((x ** 2) + (y ** 2), [x, y]))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(dist)[1])
        
        return ans
        

        