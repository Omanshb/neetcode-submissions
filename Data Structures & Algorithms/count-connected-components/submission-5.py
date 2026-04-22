class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        
        for s, e in edges:
            adj[s] = adj.get(s, []) + [e]
            adj[e] = adj.get(e, []) + [s]
        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return 
            
            visited.add(curr)

            for nei in adj.get(curr, []):
                dfs(nei)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        
        return ans

"""
Intuition: please create an adjacency list. Then, once you have done that just do DFS on that list
for every single node you come across that isn't yet in visited. You should have a number for the 
total number of components in the graph.
"""