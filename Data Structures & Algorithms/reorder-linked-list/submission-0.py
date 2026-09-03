# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we find the middle of the list
        # then we reverse the second half of the list
        # then we merge the first half and the reversed second half
        if head==None:
            return None
            
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            
        # slow is pointing to the middle
        second_half_head=slow.next
        slow.next=None
        prev=None
        curr=second_half_head
        next_node=None
        while curr!=None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        slow.next=None
        left_head=head
        right_head=prev
        while right_head!=None and left_head!=None:
            left_head_next=left_head.next
            right_head_next=right_head.next
            left_head.next=right_head
            right_head.next=left_head_next
            left_head=left_head_next
            right_head=right_head_next
            
        