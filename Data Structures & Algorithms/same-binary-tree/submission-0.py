# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1=[p]
        stack2=[q]
        while len(stack1)>0 and len(stack2)>0:
            curr1=stack1.pop()
            curr2=stack2.pop()
            if curr1==None and curr2==None:
                continue
            elif curr1==None and curr2!=None:
                return False
            elif curr1!=None and curr2==None:
                return False
            elif curr1!=None and curr2!=None:
                if curr1.val!=curr2.val:
                    return False
                else:
                    stack1.append(curr1.left)
                    stack1.append(curr1.right)
                    stack2.append(curr2.left)
                    stack2.append(curr2.right)
        if len(stack1)>0 or len(stack2)>0:
            return False
        else:
            return True


        