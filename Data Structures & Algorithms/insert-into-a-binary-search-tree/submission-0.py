# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val):
        if val<root.val:
            if root.left!=None:
                self.helper(root.left, val)
            else:
                new_node=TreeNode(val)
                root.left=new_node
        else:
            if root.right!=None:
                self.helper(root.right, val)
            else:
                new_node=TreeNode(val)
                root.right=new_node


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            new_node=TreeNode(val)
            return new_node
        else:
            self.helper(root,val)
            return root
        