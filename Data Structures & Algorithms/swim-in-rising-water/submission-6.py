class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        visited = set()
        
        pq = [(grid[0][0], 0, 0)]

        while pq:
            current_dist, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return current_dist
            
            if r - 1 in range(0, n):
                heapq.heappush(pq, (max(current_dist, grid[r - 1][c]), r - 1, c))
            if r + 1 in range(0, n):
                heapq.heappush(pq, (max(current_dist, grid[r + 1][c]), r + 1, c))
            if c - 1 in range(0, n):
                heapq.heappush(pq, (max(current_dist, grid[r][c - 1]), r, c - 1))
            if c + 1 in range(0, n):
                heapq.heappush(pq, (max(current_dist, grid[r][c + 1]), r, c + 1))

        return float('inf')

"""
Intuition: we are essentially just doing dijkstra's here. The most important thing to notice is that
the cells are like nodes and their weights are the edges kinda. We do a priority queue where we go to the
next cell with the least maximum value until now. When we end up on grid[n - 1][n - 1] for the first time
that's when we can just return the value on there which is just the maximum you need to get there through
the best path.
"""