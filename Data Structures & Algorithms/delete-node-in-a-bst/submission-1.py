# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''If there is no left child, return the right child.
            If there is no right child, return the left child.
            Otherwise, find the in-order successor (leftmost node in the right subtree), copy its value to the current node, and recursively delete the successor.
        '''
        curr=root
        prev=None
        direction=None
        while curr!=None:
            if curr.val==key:
                if curr.left==None and curr.right==None:
                    if prev==None:
                        root=None
                    else:
                        if direction=="left":
                            prev.left=None
                        else:
                            prev.right=None
                    break
                elif curr.left==None and curr.right!=None:
                    if prev==None:
                        root=curr.right
                    else:
                        if direction=="left":
                            prev.left=curr.right
                        else:
                            prev.right=curr.right
                    break
                elif curr.left!=None and curr.right==None:
                    if prev==None:
                        root=curr.left
                    else:
                        if direction=="left":
                            prev.left=curr.left
                        else:
                            prev.right=curr.left
                    break
                else:
                    # left most child of the right node
                    temp=curr.right
                    prev_temp=curr
                    while temp.left!=None:
                        prev_temp=temp
                        temp=temp.left
                    curr.val=temp.val
                    if prev_temp.left==temp:
                        prev_temp.left=temp.right   # changed: preserve temp's right subtree
                    else:
                        prev_temp.right=temp.right  # handles the case where curr.right itself was the successor (no while-loop iterations)
                    break
            elif key<curr.val:
                prev=curr
                curr=curr.left
                direction="left"
            elif key>curr.val:
                prev=curr
                curr=curr.right
                direction="right"
        return root

        