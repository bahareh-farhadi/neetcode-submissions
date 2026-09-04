# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # bfs, use queue
        queue=deque()
        res=list()
        queue.appendleft(root)
        while len(queue)>0:
            elem=queue.popleft()
            if elem!=None:
                res.append(elem.val)
                queue.appendleft(elem.right)
                queue.appendleft(elem.left)
        return res
        