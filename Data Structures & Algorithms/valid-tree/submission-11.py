class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = {}

        for s, e in edges:
            adj[s] = adj.get(s, []) + [e]
            adj[e] = adj.get(e, []) + [s]
        
        visited = set()
        rec = set()

        def helper(curr, prev):
            if curr in rec:
                return True
            
            if curr in visited:
                return False
            
            visited.add(curr)
            rec.add(curr)
            
            for i in adj.get(curr, []):
                if i != prev and helper(i, curr):
                    return True
            
            rec.remove(curr)
            return False
        
        for i in adj.keys():
            if helper(i, None):
                return False
        
        return True