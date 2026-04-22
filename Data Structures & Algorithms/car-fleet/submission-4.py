class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        inp = [(position[i], speed[i]) for i in range(len(speed))]
        inp.sort(key = lambda x: x[0])
        time2dest = []
        for p, s in inp:
            time2dest.append((target - p) / s)
        
        stack = []
        for t in time2dest:
            while stack and t >= stack[-1]:
                stack.pop()
            
            stack.append(t)
        
        return len(stack)