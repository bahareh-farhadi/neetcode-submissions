"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # this one is similar to the other solution where we use 2 dictionaries, but here we only need one to store mappings of the first copy to the second copy
        if head==None:
            return None
        mapping=dict()
        new_head=Node(head.val)
        mapping[head]=new_head
        curr=head
        new_curr=new_head
        while curr.next!=None:
            curr=curr.next
            new_node=Node(curr.val)
            mapping[curr]=new_node
            new_curr.next=new_node
            new_curr=new_node
        new_curr.next=None
        curr=head
        new_curr=new_head
        while curr!=None:
            if curr.random!=None:
                new_curr.random=mapping[curr.random]
            curr=curr.next
            new_curr=new_curr.next
        return new_head
        