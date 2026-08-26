class MyQueue:
    # amoirtized complexity solution - so it is sometimes O(n) and sometimes O(1). in this case we pop from s2 if s2 has any elements, but if it is empty we first move all elements from s1 to s2 and then pop from s2.
    def __init__(self):
        self.s1=list()
        self.s2=list()
        

    def push(self, x: int) -> None:
        self.s1.append(x)
    
        

    def pop(self) -> int:
        if len(self.s2)==0:
            while len(self.s1)>0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        if len(self.s2)==0:
            while len(self.s1)>0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        
        

    def empty(self) -> bool:
        if len(self.s1)==0 and len(self.s2)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()