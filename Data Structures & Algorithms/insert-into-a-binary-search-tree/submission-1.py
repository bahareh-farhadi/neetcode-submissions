# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            new_node=TreeNode(val)
            return new_node
        else:
            curr=root
            while True:
                if curr.val>val:
                    if curr.left==None:
                        curr.left=TreeNode(val)
                        break
                    else:
                        curr=curr.left
                else:
                    if curr.right==None:
                        curr.right=TreeNode(val)
                        break
                    else:
                        curr=curr.right
            return root
        