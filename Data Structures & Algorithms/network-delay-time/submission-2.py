class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []
        
        adj = {}

        for s, e, t in times:
            adj[s] = adj.get(s, []) + [[t, e]]
        
        heapq.heappush(pq, [0, 0, k])

        visited = set()
        mx = 0

        while len(visited) < n and pq:
            curr, cost, nxt = heapq.heappop(pq)
            if nxt not in visited:
                visited.add(nxt)
                mx = max(mx, curr)
                for nei in adj.get(nxt, []):

                    nei = [curr + nei[0]] + nei
                    heapq.heappush(pq, nei)
        
        return mx if len(visited) == n else -1
