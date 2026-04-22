class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if min(i, j) < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1
        return counter