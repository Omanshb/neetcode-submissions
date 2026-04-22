class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[(x1, y1)] = adj.get((x1, y1), []) + [(dist, x2, y2)]
                adj[(x2, y2)] = adj.get((x2, y2), []) + [(dist, x1, y1)]
        
        pq = [(0, points[0][0], points[0][1])]
        visited = set()

        ans = 0
        while len(visited) != len(points) and pq:
            edge_cost, x, y = heapq.heappop(pq)
            if (x, y) not in visited:
                visited.add((x, y))
                ans += edge_cost
                for nei in adj.get((x, y), []):
                    heapq.heappush(pq, (nei))
        
        return ans