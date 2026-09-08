# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_height=0
    def helper(self, root):
        if root==None:
            return 0
        else:
            global max_height
            left_height=self.helper(root.left)
            right_height=self.helper(root.right)
            max_height=max(max_height, left_height+right_height)
            return 1+max(left_height, right_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_height
        max_height=0
        self.helper(root)
        return max_height

        
        