# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res=0
    def helper(self, max_val, root):
        if root.val>=max_val:
            max_val=root.val
            global res
            res+=1
        if root.left!=None:
            self.helper(max_val, root.left)
        if root.right!=None:
            self.helper(max_val, root.right)

    def goodNodes(self, root: TreeNode) -> int:
        global res
        res=0
        self.helper(-100, root)
        return res
        