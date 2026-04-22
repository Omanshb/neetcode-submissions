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

"""
Intuition: Start off by making a directed adjacency list of the courses and each of their prerequisites.
Then, have a visited and a recursion stack. Essentially, we're just doing a cycle check. from each of the
classes. The base case is that the current class is already in the recursion stack in which case you return True
Otherwise, if curr is already in visited you return False. Then you add curr to visited and recursion
and continue downwards the graph. If there is a single true (cycle) then please return False (the
classes are not completable.)
"""