# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count=1
        curr=head
        prev_prev=None
        while count<left:
            prev_prev=curr
            curr=curr.next
            count+=1
        prev=None
        next_node=None
        last_node=None
        while count<=right:
            next_node=curr.next
            if prev==None:
                last_node=curr
            curr.next=prev
            prev=curr
            curr=next_node
            count+=1
        if prev_prev!=None:
            prev_prev.next=prev
            new_head=head
        else:
            new_head=prev
        last_node.next=next_node
        return new_head

        