class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif c == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif c == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return not stack

"""
Intuition: Very easy stack problem. If it's (, {, or [, then just add it to the end 
of the stack .If it's ), }, or ], then check the end of the stack to make sure the
most recent character matches the corresponding closing bracket. If so, pop from the 
stack because we can consider that pairing "done". If not, or if the stack is empty,
return False. At the end, just check if the stack is empty (all opening brackets have
met their closing bracket).

Time Complexity: O(n) because we're just doing an O(1) operation across the list.

Space Complexity: O(n) because we're just holding a stack that grows at most to 
the length of the string.
"""