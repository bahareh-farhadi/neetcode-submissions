# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        stack=list()
        stack.append((root, 1))
        max_depth=1
        while len(stack)>0:
            curr_node, curr_depth=stack.pop()
            max_depth=max(max_depth, curr_depth)
            if curr_node.left!=None:
                stack.append((curr_node.left, curr_depth+1))
            if curr_node.right!=None:
                stack.append((curr_node.right, curr_depth+1))
        return max_depth
        