class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                curr = []
                if i - 1 in range(0, len(grid)):
                    curr.append((grid[i - 1][j], i - 1, j))
                if i + 1 in range(0, len(grid)):
                    curr.append((grid[i + 1][j], i + 1, j))
                if j - 1 in range(0, len(grid[i])):
                    curr.append((grid[i][j - 1], i, j - 1))
                if j + 1 in range(0, len(grid[i])):
                    curr.append((grid[i][j + 1], i, j + 1))
                row.append(curr)
            adj.append(row)
        
        max_in_path = [[-float('inf')] * len(grid[i]) for i in range(len(grid))]
        visited = set()
        
        pq = [(grid[0][0], grid[0][0], 0, 0)]
        while len(visited) < len(grid) * len(grid[0]) and pq:
            weight, mx, x, y = heapq.heappop(pq)

            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            max_in_path[x][y] = max(mx, weight)

            for nei in adj[x][y]:
                heapq.heappush(pq, (nei[0], max_in_path[x][y], nei[1], nei[2]))
        
        return max_in_path[len(grid) - 1][len(grid[0]) - 1]



