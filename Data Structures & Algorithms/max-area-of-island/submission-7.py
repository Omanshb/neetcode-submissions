class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            nonlocal mx

            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            val = 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)

            return val
        
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    mx = max(dfs(i, j), mx)
        
        return mx

"""
Intuition: Every time that you end up on a square that's 1, you perform DFS
on it. Then, in that DFS, you recursively spread out to all of the other 1s
that are on that same island and you add 1 every time u clear an island spot.
For every DFS performed, you just keep a running max as the answer for the end.
"""