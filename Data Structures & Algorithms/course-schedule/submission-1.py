class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = {i:[] for i in range(numCourses)}

        for prerequisite in prerequisites:
            preqs[prerequisite[1]].append(prerequisite[0])
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            cycle = True
            visited.add(course)
            for c in preqs[course]:
                if not dfs(c):
                    cycle = False
            visited.remove(course)
            return cycle
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True