class Node:
    def __init__(self, val: int):
        self.val=val
        self.next=None
        self.parent=None

class MyCircularQueue:
    def __init__(self, k: int):
        self.k=k
        self.head=None
        prev=None
        for i in range(self.k):
            new_node=Node(-1)
            if self.head==None:
                self.head=new_node
            else:
                new_node.parent=prev
                prev.next=new_node
            prev=new_node
        self.head.parent=new_node
        new_node.next=self.head

        

    def enQueue(self, value: int) -> bool:
        if self.isFull()==False:
            curr=self.head
            for i in range(self.k):
                if curr.val!=-1:
                    curr=curr.next
                else:
                    break
            curr.val=value
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head.val=-1
            self.head=self.head.next
            return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            curr=self.head
            for i in range(self.k):
                if curr.next.val!=-1:
                    curr=curr.next
                else:
                    break
            if curr==self.head:
                # when all elements are full or there is only one element
                if self.isFull():
                    return self.head.parent.val
                else:
                    return self.head.val
            else:
                return curr.val
        

    def isEmpty(self) -> bool:
        if self.head.val==-1:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.head.parent.val==-1:
            return False
        else:
            return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()