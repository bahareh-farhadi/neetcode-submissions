# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        

        curr=None
        new_head=None
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                if curr==None:
                    curr=list1
                    new_head=curr
                else:
                    curr.next=list1
                    curr=curr.next
                list1=list1.next
            else:
                if curr==None:
                    curr=list2
                    new_head=curr
                else:
                    curr.next=list2
                    curr=curr.next
                list2=list2.next
            
        while list1!=None:
            if curr==None:
                curr=list1
                new_head=curr
            else:
                curr.next=list1
                curr=curr.next
            list1=list1.next
            
        while list2!=None:
            if curr==None:
                curr=list2
                new_head=curr
            else:
                curr.next=list2
                curr=curr.next
            list2=list2.next
        curr.next=None
        return new_head


        