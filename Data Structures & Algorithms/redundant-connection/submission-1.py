class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {}

        def dfs(node, par):
            if node in visit:
                return True

            visit.add(node)
            for nei in adj.get(node):
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adj[u] = adj.get(u, []) + [v]
            adj[v] = adj.get(v, []) + [u]
            visit = set()

            if dfs(u, -1):
                return [u, v]
        return []