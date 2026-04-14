class MinStack:

    def __init__(self):
        self.MinStack = []
        self.ExtraStack = []
    def push(self, val: int) -> None:
        self.MinStack.append(val)
        val = min(val, self.ExtraStack[-1] if self.ExtraStack else val)
        self.ExtraStack.append(val)
        return self.MinStack

    def pop(self) -> None:
        self.ExtraStack.pop()
        return self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.ExtraStack[-1]