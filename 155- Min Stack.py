class MinStack(object):

    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x):
        self.A.append(x)
        self.B.append( x if not self.B else min(x, self.B[-1]))

    def pop(self):
        self.A.pop()
        self.B.pop()

    def top(self):
        return self.A[-1]

    def getMin(self):
        return self.B[-1]