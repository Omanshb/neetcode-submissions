class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        totalCost = 0

        pq = [(0, points[0])]

        while len(pq) != 0:
            distance, point = heapq.heappop(pq)

            if tuple(point) in visited:
                continue 
            
            totalCost += distance
            visited.add(tuple(point))

            for p in points:
                if tuple(p) not in visited:
                    dist = abs(point[0] - p[0]) + abs(point[1] - p[1])
                    heapq.heappush(pq, (dist, p))
        
        return totalCost