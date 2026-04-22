class MinStack:

    def __init__(self):
        self.stk = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.mins.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mins[-1]

