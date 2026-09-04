# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # use dfs, use a stack 
        stack=list()
        curr=root
        res=list()
        while curr!=None or len(stack)>0:
            while curr!=None:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res
            
            
        