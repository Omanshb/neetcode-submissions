class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 + n1)
            elif c == "-":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 - n1)
            elif c == "*":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 * n1)
            elif c == "/":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 / n1)
            else:
                stack.append(c)
        return int(stack[0])

"""
Intuition: Very basic stack problem once again. Every time you see a new operation, 
you just pop the two numbers from the stack, calculate the value, and then append it.
Then, at the end, you just return the only number left in the stack. This problem is 
very simple because you are guaranteed that the reverse polish notation will be valid.

Time Complexity: O(n) because every operation on the tokens as we iterate is just O(1)
Space Complexity: O(n) because at most, we are just holding a stack of n characters/numbers.
"""