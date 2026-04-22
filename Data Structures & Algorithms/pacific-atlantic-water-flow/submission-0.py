class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacificAccessible = set()
        atlanticAccessible = set()

        def dfs(i, j, prev, ocean):
            if min(i, j) < 0 or i >= len(heights) or j >= len(heights[i]) or heights[i][j] < prev or (i, j) in ocean:
                return
            
            ocean.add((i, j))
            dfs(i - 1, j, heights[i][j], ocean)
            dfs(i + 1, j, heights[i][j], ocean)
            dfs(i, j + 1, heights[i][j], ocean)
            dfs(i, j - 1, heights[i][j], ocean)


        for i in range(len(heights[0])):
            dfs(0, i, -float('inf'), pacificAccessible)
            dfs(len(heights) - 1, i, -float('inf'), atlanticAccessible)
        for j in range(len(heights)):
            dfs(j, 0, -float('inf'), pacificAccessible)
            dfs(j, len(heights[0]) - 1, -float('inf'), atlanticAccessible)
        
        return [list(x) for x in pacificAccessible & atlanticAccessible]