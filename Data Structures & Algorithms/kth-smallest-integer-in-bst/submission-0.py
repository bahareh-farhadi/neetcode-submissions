# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=list()
        res=list()
        curr=root
        while curr!=None or len(stack)>0:
            if len(res)==k:
                break
            while curr!=None:
                stack.append(curr)
                curr=curr.left
            elem=stack.pop()
            res.append(elem.val)
            curr=elem.right
        return res[-1]
        