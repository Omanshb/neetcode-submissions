class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        opposites = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for c in s:
            if c in opposites:
                if len(stck) == 0:
                    return False
                if opposites[c] != stck[-1]:
                    return False
                stck.pop()
            else:
                stck.append(c)
        return len(stck) == 0