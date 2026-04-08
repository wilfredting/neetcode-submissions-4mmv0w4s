class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.curr_min.append(val)
        else:
            self.curr_min.append(min(val, self.curr_min[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1]
        
