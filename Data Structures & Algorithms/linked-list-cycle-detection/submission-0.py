# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        slow=head
        fast=head
        while fast!=None:
            if fast.next==slow:
                return True
            else:
                fast=fast.next
                if fast==None:
                    return False
                fast=fast.next
                slow=slow.next
        return False
        