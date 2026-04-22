class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for s, d, cost in flights:
            adj[s] = adj.get(s, []) + [(d, cost)]
        
        pq = [(0, 0, src)]
        
        while pq:
            cost, flights, loc = heapq.heappop(pq)

            if flights > k + 1:
                continue

            if loc == dst:
                return cost
            
            for nxt, travel_cost in adj.get(loc, []):
                heapq.heappush(pq, (cost + travel_cost, flights + 1, nxt))
        
        return -1