class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
    
class LRUCache:
    # the idea is to use a doubly linked list and hash map
    # the hash map-> key: key, value: address of the node 
    # we make sure the most recently used node is always at head and the least recently used node is always at the tail. when we get a node we move it to head. when we put a new node we add it to head. if when putting a new node we are exceeding the capacity we first remove the element at the tail and then add the new node at the head.

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.curr_size=0
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.seen=dict()
        

    def get(self, key: int) -> int:
        if key in self.seen:
            # most recently used so move to head
            node=self.seen[key]
            prev_node=node.prev
            next_node=node.next
            prev_node.next=next_node
            next_node.prev=prev_node
            head_next=self.head.next
            self.head.next=node
            node.prev=self.head
            node.next=head_next
            head_next.prev=node
            return node.val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            # update the value and then move to head
            node=self.seen[key]
            node.val=value
            prev_node=node.prev
            next_node=node.next
            prev_node.next=next_node
            next_node.prev=prev_node
            head_next=self.head.next
            self.head.next=node
            node.prev=self.head
            node.next=head_next
            head_next.prev=node
        else:
            # add a new node and item in dict
            node=Node(key, value)
            self.seen[key]=node
            if self.curr_size<self.capacity:
                #can add a new node without deleting any
                head_next=self.head.next
                self.head.next=node
                node.prev=self.head
                node.next=head_next
                head_next.prev=node
                self.curr_size+=1
            else:
                #delete the node at the tail
                lru=self.tail.prev
                lru_prev=lru.prev
                del self.seen[lru.key]
                lru_prev.next=self.tail
                self.tail.prev=lru_prev
                head_next=self.head.next
                self.head.next=node
                node.prev=self.head
                node.next=head_next
                head_next.prev=node
                self.curr_size+=1
                

            
        
