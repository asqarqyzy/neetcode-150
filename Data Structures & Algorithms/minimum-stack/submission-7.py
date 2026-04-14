class MinStack:

    def __init__(self):
        self.MinStack = []
        self.ExtraStack = []
        self.min_el = None
    def push(self, val: int) -> None:
        if len(self.MinStack) == 0:
            self.ExtraStack.append(val)
            self.min_el = self.ExtraStack[-1]
        elif val <= self.ExtraStack[-1]:
            self.ExtraStack.append(val)
            self.min_el = self.ExtraStack[-1]
        return self.MinStack.append(val)

    def pop(self) -> None:
        if self.MinStack[-1] == self.min_el:
            self.ExtraStack.pop()
            if len(self.ExtraStack) > 0:
                self.min_el = self.ExtraStack[-1]
        return self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.min_el