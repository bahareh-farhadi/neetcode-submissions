class FreqStack:
    # the idea is to have a stack that contains multiple stacks
    # we have to keep a hash map to keep track of frequency of each number.
    # when a new element is pushed we check its frequency, if its one it will get added to the first stack, if its 2 it will get added to the 2nd stack and so on. 
    # then we want to pop we start popping from the last stack backwards (the last stack is basically like the last element of the main stack so it makes sense)
    def __init__(self):
        self.stack=list()
        self.freq=dict()
        self.num_stacks=0
        

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val]+=1
        else:
            self.freq[val]=1
        if self.freq[val] <=self.num_stacks:
            self.stack[self.freq[val]-1].append(val)
        else:
            new_stack=[val]
            self.stack.append(new_stack)
            self.num_stacks+=1
        
        

    def pop(self) -> int:
        elem=self.stack[-1].pop()
        self.freq[elem]-=1
        if self.freq[elem]==0:
            self.freq.pop(elem)
        if len(self.stack[-1])==0:
            self.stack.pop()
            self.num_stacks-=1
        return elem
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()