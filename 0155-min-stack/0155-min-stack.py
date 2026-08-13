class MinStack:

    def __init__(self):
        self.st=[]
        self.st2=[]
        self.min=float('inf')
    def push(self, value: int) -> None:
        self.st.append(value)
        if value<=self.min:
            self.min=value
            self.st2.append(value)
    def pop(self) -> None:
        x = self.st.pop()
        if x == self.min:
            self.st2.pop()

        if self.st2:
            self.min = self.st2[-1]
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()