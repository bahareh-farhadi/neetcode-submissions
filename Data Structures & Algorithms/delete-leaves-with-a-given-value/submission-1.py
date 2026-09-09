# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # simpler solution, just use a postorder (LRM) traversal
    def helper(self, root, target):
        if root==None:
            return None
        res_left=self.helper(root.left, target)
        res_right=self.helper(root.right, target)
        if res_left==None and res_right==None and root.val==target:
            return None
        else:
            root.left=res_left
            root.right=res_right
            return root
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.helper(root, target)
        