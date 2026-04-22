class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj= {}

        for c, p in prerequisites:
            adj[c] = adj.get(c, []) + [p]
        
        visited = set()
        rec = set()
    
        def helper(curr):
            if curr in rec:
                return True
            
            if curr in visited:
                return False
            
            visited.add(curr)
            rec.add(curr)

            for i in adj.get(curr, []):
                if helper(i):
                    return True
            
            rec.remove(curr)
            return False
        
        for i in adj.keys():
            if i not in visited and helper(i):
                    return False
        
        return True