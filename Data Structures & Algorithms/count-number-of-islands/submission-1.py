class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans

"""
Intuition: Iterate through the entire grid one by one. Every time you see
a grid spot that's 1, start doing DFS over it and then change the grid spot
to 0 every time you come across it. At the end, count how many different
times you had to do DFS (once for each island)
"""