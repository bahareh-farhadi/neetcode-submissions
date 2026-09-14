# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # since this is a bst, if both p and q are less than the current node then the lca is in the left subtree, if both p and q are greater than the current node then the lca is in the right subtree, and if e.g. p is less than or equal to the current node but q is greater than or equal to the current node then the current node is the lca. 
        curr=root
        while True:
            if p.val<curr.val and q.val<curr.val:
                curr=curr.left
            elif p.val>curr.val and q.val>curr.val:
                curr=curr.right
            else:
                return curr
                
        