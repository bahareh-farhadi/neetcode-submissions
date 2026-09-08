# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def helper(self, root, subRoot):
        # this function checks for EXACT match
        if root==None:
            if subRoot==None:
                return True
            else:
                return False
        else:
            if subRoot==None:
                return False
            else:
                if root.val==subRoot.val:
                    return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)
                else:
                    return False 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None:
            return True # an empty subtree is always a subtree
        elif root==None:
            return False # an empty tree has no subtrees
        else:
            if self.helper(root, subRoot)==True:
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        