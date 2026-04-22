class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for s, e, t in times:
            adj[s] = adj.get(s, []) + [(t, e)]
        
        distances = [float('inf')] * (n + 1)
        
        pq = [(0, k)]

        while pq:
            cost, nxt = heapq.heappop(pq)
            if cost < distances[nxt]:
                distances[nxt] = cost
                for nei in adj.get(nxt, []):
                    heapq.heappush(pq, (nei[0] + cost, nei[1]))
        
        mx = max(distances[1:])
        return mx if mx != float('inf') else -1


"""
Intuition: This is just dijskstra's algorithm. We are creating an adjacency list to properly represent the
graph. Then, we initialize a heap which will help guide our algorithm in terms of where to go next and a 
distances list which will keep track of the minimum distances from our starting node to all of the other ones.
With a given node, we check if the current cost is < distances[nxt] and update accordingly. Then, for every 
neighbor, we add them to the heap with the current cost + the new neighbor edge cost. At the end, just return
the maximum distance if it's not infinity otherwise return -1 since it means not every node was reached.
"""