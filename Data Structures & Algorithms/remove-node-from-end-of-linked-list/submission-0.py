# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        curr=head
        prev=None
        target=None
        next_node=None
        while curr!=None:
            k+=1
            if k==n:
                target=head
            elif k>n:
                prev=target
                target=target.next
            curr=curr.next
        if prev==None:
            # deleting the first node
            head=target.next
        else:
            prev.next=target.next
        return head

                


        