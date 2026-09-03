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
        if head==None:
            return None
        seen=dict()
        new_seen=dict()
        new_head=Node(head.val)
        count=0
        seen[head]=count
        new_seen[count]=new_head
        curr=head
        new_curr=new_head
        while curr.next!=None:
            curr=curr.next
            new_node=Node(curr.val)
            count+=1
            seen[curr]=count
            new_seen[count]=new_node
            new_curr.next=new_node
            new_curr=new_node
        new_curr.next=None
        curr=head
        new_curr=new_head
        while curr!=None:
            if curr.random!=None:
                index=seen[curr.random]
                new_curr.random=new_seen[index]
            curr=curr.next
            new_curr=new_curr.next
        return new_head
        