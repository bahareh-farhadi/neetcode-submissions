# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ITERATIVE SOLUTION
class Solution:
    def helper(self, root, key):
        if root==None:
            return None
        if root.val==key:
            if root.left==None and root.right==None:
                return None
            elif root.left==None and root.right!=None:
                return root.right
            elif root.left!=None and root.right==None:
                return root.left
            else:
                temp=root.right
                temp_prev=root
                while temp.left!=None:
                    temp_prev=temp
                    temp=temp.left
                root.val=temp.val
                if temp==root.right:
                    # no loop was done
                    temp_prev.right=temp.right
                else:
                    temp_prev.left=temp.right
                return root
        elif key<root.val:
            root.left=self.helper(root.left, key)
        elif key>root.val:
            root.right=self.helper(root.right, key)
        return root
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''If there is no left child, return the right child.
            If there is no right child, return the left child.
            Otherwise, find the in-order successor (leftmost node in the right subtree), copy its value to the current node, and recursively delete the successor.
        '''
        return self.helper(root, key)

        

        