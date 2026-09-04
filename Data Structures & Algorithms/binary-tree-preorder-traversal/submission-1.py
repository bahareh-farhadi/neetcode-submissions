# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=deque()
        res=list()
        stack.appendleft(root)
        while len(stack)>0:
            elem=stack.popleft()
            if elem!=None:
                res.append(elem.val)
                stack.appendleft(elem.right)
                stack.appendleft(elem.left)
        return res
        