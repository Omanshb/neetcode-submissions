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

"""
Intuition: The first thing we need to do is sort the cars based on position in ascending
order. Then, once we have done that, we need to calculate the time-to-destination for 
each of the cars. The only way that a car will merge with the cars before it is if the
time-to-destination for that car is greater than the ones preceeding it. For this reason,
we can keep track of a stack for this problem. For every new car, we keep popping off of the
list as long as the time-to-destination for those previous cars is less than the current one.
Then, we simply append the current car. This popping action is essentially just us "merging" 
the cars that should belong in one fleet together. At the end, we just have to return the length
of the stack.

Time Complexity: O(n) because at every point, we are doing O(1) operations.

Space Complexity: O(n) because we have to maintain a stack at all times with the fleets
that can grow to length n at most.
"""