# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root.left!=None:
            left_res, left_height=self.helper(root.left)
        else:
            left_height=0
            left_res=True
        if root.right!=None:
            right_res, right_height=self.helper(root.right)
        else:
            right_height=0
            right_res=True
        if left_res==False or right_res==False:
            return False, None
        else:
            if abs(left_height-right_height)>1:
                return False, None
            else:
                curr_height=1+max(left_height, right_height)
                return True, curr_height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        res, _ = self.helper(root)
        return res
        