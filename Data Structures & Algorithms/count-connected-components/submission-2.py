class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for frm, to in edges:
            adj[frm].append(to)
            adj[to].append(frm)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
                
            visited.add(node)
            for n in adj[node]:
                dfs(n)
        
        counter = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                counter += 1

        return counter