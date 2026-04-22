class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for c, p in prerequisites:
            adj[c] = adj.get(c, []) + [p]
        
        visited = set()
        rec = set()
        order = []

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
            order.append(curr)

            return False
        
        for i in range(numCourses):
            if i not in visited:
                if helper(i):
                    return []
        
        return order