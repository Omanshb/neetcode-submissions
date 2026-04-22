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