# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        head=None
        prev=None
        carry=0
        while curr1!=None and curr2!=None:
            temp=curr1.val+curr2.val+carry
            carry=int(temp/10)
            current_val=temp%10
            new_node=ListNode(current_val)
            if head==None:
                head=new_node
            else:
                prev.next=new_node
            prev=new_node
            curr1=curr1.next
            curr2=curr2.next
        while curr1!=None:
            temp=curr1.val+carry
            carry=int(temp/10)
            current_val=temp%10
            new_node=ListNode(current_val)
            if head==None:
                head=new_node
            else:
                prev.next=new_node
            prev=new_node
            curr1=curr1.next
        while curr2!=None:
            temp=curr2.val+carry
            carry=int(temp/10)
            current_val=temp%10
            new_node=ListNode(current_val)
            if head==None:
                head=new_node
            else:
                prev.next=new_node
            prev=new_node
            curr2=curr2.next
        if carry>0:
            new_node=ListNode(carry)
            prev.next=new_node
            prev=new_node
        prev.next=None
        return head
            
            
       
            

        