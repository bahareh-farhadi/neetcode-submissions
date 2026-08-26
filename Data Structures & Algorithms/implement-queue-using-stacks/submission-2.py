class MyQueue:
    # the idea of this is similar to "Implement Stack using Queues"
    # we use 2 stacks, we move all elements from stack 1 to 2, then we push to stack 2, then we move all elements from s2 to s1
    def __init__(self):
        self.s1=list()
        self.s2=list()
        

    def push(self, x: int) -> None:
        while len(self.s1)>0:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while len(self.s2)>0:
            self.s1.append(self.s2.pop())
    
        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        if len(self.s1)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()