from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None
        visited=set()
        queue=deque()
        queue.append(node)
        visited.add(node.val)
        new_head=Node(node.val)
        mapping=dict()
        mapping[node]=new_head
        while len(queue)>0:
            curr=queue.popleft()
            curr_copy=mapping[curr]
            for n in curr.neighbors:
                if n.val not in visited:
                    visited.add(n.val)
                    queue.append(n)
                    n_new=Node(n.val)
                    mapping[n]=n_new
                else:
                    n_new=mapping[n]
                curr_copy.neighbors.append(n_new)
        return new_head
            

        