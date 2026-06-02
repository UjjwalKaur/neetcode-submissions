class MinStack:

    def __init__(self):
        self.vals = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.vals.append(val)
        if self.min:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)
        
    def pop(self) -> None:
        self.vals.pop()
        self.min.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min[-1]

        
