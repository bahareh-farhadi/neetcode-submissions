# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        stack=deque()
        stack.append((root, 0))
        res=list()
        while len(stack)>0:
            curr=stack.popleft()
            if len(stack)==0 or stack[0][1]!=curr[1]:
                res.append(curr[0].val)
            if curr[0].left!=None:
                stack.append((curr[0].left, curr[1]+1))
            if curr[0].right!=None:
                stack.append((curr[0].right, curr[1]+1))
        return res
        