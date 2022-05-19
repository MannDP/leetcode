class MinStack:

    def __init__(self):
        self.items = list()

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append((val, val))
        else:
            mmin = min(self.items[-1][1], val)
            self.items.append((val, mmin))

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
