class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for parenthesis in s:
            if parenthesis == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
            elif parenthesis == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
            elif parenthesis == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(parenthesis)
        return not stack
            