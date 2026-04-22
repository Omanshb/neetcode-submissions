class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = [(0, points[0][0], points[0][1])]
        visited = set()

        ans = 0
        while len(visited) != len(points) and pq:
            edge_cost, x1, y1 = heapq.heappop(pq)
            if (x1, y1) not in visited:
                visited.add((x1, y1))
                ans += edge_cost

                for p in points:
                    if tuple(p) not in visited:
                        x2, y2 = p
                        heapq.heappush(pq, (abs(x1 - x2) + abs(y1 - y2), x2, y2))

        
        return ans

"""
Intuition: This is literally just prim's algorithm for finding an MST. At any given point, we just
take the top of the priority queue of all the nearby edges and then if any of them lead to nodes that
we haven't yet seen, we add the node to visited, use that edge to expand our spanning tree, and then
update our heap with all of the newly accessible nodes + their distance away. At any given point, we are
just taking the cheapest option for expanding the MST.
"""