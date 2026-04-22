class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
"""
Intuition: Pretty neat problem. Essentially, alongside the regular stack, we also 
have to keep track of a min stack. For every element in the regular stack, there 
is an element in the min stack that represents the minimum at the time that element
was added to the array. This means that for every new element addition, we just
do mins.append(min(mins[-1], val)). It would look kinda like this

Regular Stack: [1, 4, 2, 9, 0, 8, 1]
Min Stack: [1, 1, 1, 1, 0, 0, 0]

Then, every time we pop, we also pop from the min stack. This means that when, for
example the 0 gets popped, it also gets removed as the min.

Time Complexity: All operations are in O(n) time.
Space Complexity: Regular stack and min stack so O(n) space.
"""