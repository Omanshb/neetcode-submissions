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
