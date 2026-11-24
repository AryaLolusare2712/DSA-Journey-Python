class MinStack(object):

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        minval = min(value, self.MinStack[-1] if self.MinStack else value)
        self.MinStack.append(minval)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.MinStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()