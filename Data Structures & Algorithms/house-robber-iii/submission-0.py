# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=0
    def helper(self, root):
        if root==None:
            return 0,0
        left_child, left_grandchild=self.helper(root.left)
        right_child, right_grandchild=self.helper(root.right)
        can_rob_now=root.val+left_grandchild+right_grandchild
        cannot_rob_now=max(left_child, left_grandchild)+max(right_child, right_grandchild)
        Solution.res=max(Solution.res, can_rob_now, cannot_rob_now)
        return can_rob_now, cannot_rob_now

        
    def rob(self, root: Optional[TreeNode]) -> int:
        Solution.res=0
        self.helper(root)
        return Solution.res

        