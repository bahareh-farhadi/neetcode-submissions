# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we have to make sure each node is in the right range.
        # when we move towards left the maximum value the left subtree can have is the value of the current node, and when we move towards the right subtree the minimum value the right subtree can have is the value of the current node
        queue=deque()
        queue.append((root, -float('inf'), float('inf')))
        while len(queue)>0:
            curr=queue.popleft()
            curr_node=curr[0]
            curr_min=curr[1]
            curr_max=curr[2]
            
            if curr_node.val>curr_min and curr_node.val<curr_max:
                if curr_node.left!=None:
                    queue.append((curr_node.left, curr_min, curr_node.val))
                if curr_node.right!=None:
                    queue.append((curr_node.right, curr_node.val, curr_max))
            else:
                return False
        return True


        
        