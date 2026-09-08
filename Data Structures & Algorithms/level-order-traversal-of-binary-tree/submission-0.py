# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        stack=deque()
        stack.append((root, 0))
        res=list()
        while len(stack)>0:
            curr=stack.popleft()
            if curr[0].left!=None:
                stack.append((curr[0].left, curr[1]+1))
            if curr[0].right!=None:
                stack.append((curr[0].right, curr[1]+1))
            if len(res)>curr[1]:
                res[curr[1]].append(curr[0].val)
            else:
                res.append([curr[0].val])
        return res
        