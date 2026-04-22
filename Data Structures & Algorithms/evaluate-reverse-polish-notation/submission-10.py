class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            try:
                stk.append(int(t))
            except ValueError:
                print(stk, t)
                o2 = stk.pop()
                o1 = stk.pop()
                if t == "+":
                    stk.append(o1 + o2)
                elif t == "-":
                    stk.append(o1 - o2)
                elif t == "*":
                    stk.append(o1 * o2)
                else:
                    stk.append(int(float(o1) / o2))
        return stk[0]