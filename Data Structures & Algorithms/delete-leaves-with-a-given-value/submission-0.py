# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, target):
        if root.left==None and root.right==None:
            if root.val==target:
                return None
            else:
                return root
        if root.left!=None:
            res_left=self.helper(root.left, target)
            if res_left==None:
                if root.right==None:
                    if root.val==target:
                        return None
            root.left=res_left
        if root.right!=None:
            res_right=self.helper(root.right, target)
            if res_right==None:
                if root.left==None:
                    if root.val==target:
                        return None
            root.right=res_right
        return root
        


    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.helper(root, target)
        