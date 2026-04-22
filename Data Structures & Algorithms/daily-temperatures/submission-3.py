class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                popped = stack.pop()
                ans[popped[1]] = i - popped[1]

            stack.append((t, i))
        
        return ans

"""
Intuition: You simply use a stack with tuples so that you can track the index of temp
you are analyzing. For every new value we want to add, you keep popping from the stack
as long as the values are smaller. Then, for these small values, you set their answers
in the ans array as i - popped[1] (time until warmer temperature). The default value
is 0 anyways so you don't need to process anything at the end.

Time Complexity: O(n) since every operation with a new temperature is just O(1)

Space Complexity: O(n) because at most, you'll have a stack with n temperatures and 
their indices.
"""


