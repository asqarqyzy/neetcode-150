class MinStack:

    def __init__(self):
        self.MinStack = []
    def push(self, val: int) -> None:
        return self.MinStack.append(val)

    def pop(self) -> None:
        return self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return min(self.MinStack)
