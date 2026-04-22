class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        visited = set()
        
        pq = [(grid[0][0], 0, 0)]

        while len(visited) < n * n and pq:
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



