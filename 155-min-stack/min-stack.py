class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []


    def push(self, value: int) -> None:
        if not self.min or self.min[-1] >= value:
            self.min.append(value)
        self.stack.append(value)
        

    def pop(self) -> None:
        if self.stack: 
            if self.min[-1] == self.stack[-1]:
               self.min.pop()
            self.stack.pop()
        
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna