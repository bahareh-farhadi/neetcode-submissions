# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we keep a hashmap of the numbers and their indices in the inorder list
# because we do this we can't change inorder everytime as we pass it to the function, but what we have to do is to keep the boundaries of it
class Solution:
    def helper(self, preorder, inorder, indices, preorder_start, preorder_end, inorder_start, inorder_end):
        if inorder_start>inorder_end or preorder_start>preorder_end:
            return None
        root=TreeNode(preorder[preorder_start])
        root_index=indices[preorder[preorder_start]]
        left_length=root_index-inorder_start
        root.left=self.helper(preorder, inorder, indices, preorder_start+1, preorder_start+left_length,inorder_start, root_index-1)
        root.right=self.helper(preorder, inorder, indices, preorder_start+1+left_length, preorder_end,root_index+1, inorder_end)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices=dict()
        for i in range(len(inorder)):
            indices[inorder[i]]=i
        return self.helper(preorder, inorder, indices, 0, len(preorder)-1, 0, len(inorder)-1)
        