class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ")}]":
                if not stk:
                    return False
                elif (c == ')' and stk[-1] == '(') or (c == ']' and stk[-1] == '[') or (c == '}' and stk[-1] == '{'):
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return not stk
        