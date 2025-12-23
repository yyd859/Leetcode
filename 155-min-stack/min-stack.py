class MinStack:
    #first try
    # def __init__(self):
    #     self.list = []

    # def push(self, val: int) -> None:
    #     self.list.append(val)

    # def pop(self) -> None:
    #     self.list.pop()

    # def top(self) -> int:
    #     return self.list[-1]

    # def getMin(self) -> int:
        # if self.list:
        #     return min(self.list)
        # else:
        #     return self.list
        # however it is O(N), our target is O(1)
        # We will have a stack only for minimum
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()