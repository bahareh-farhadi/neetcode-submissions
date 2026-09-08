# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder is LRM, and preorder is MLR, so posorder is basically MRL in reverse. so if we do a modified version of preorder and then reverse the array we have postorder
        if root==None:
            return []
        res=list()
        stack=deque()
        stack.append(root)
        while len(stack)>0:
            elem=stack.popleft()
            res.append(elem.val)
            if elem.left!=None:
                stack.appendleft(elem.left)
            if elem.right!=None:
                stack.appendleft(elem.right)
        res.reverse()
        return res
        