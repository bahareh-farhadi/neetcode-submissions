class MinStack:

    def __init__(self):
        self.s=list()
        self.min_s=list()
        

    def push(self, val: int) -> None:
        if len(self.s)>0:
            new_min=min(val, self.min_s[-1])
        else:
            new_min=val
        self.s.append(val)
        self.min_s.append(new_min)
        

    def pop(self) -> None:
        self.s.pop()
        self.min_s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min_s[-1]
        
