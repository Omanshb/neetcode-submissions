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