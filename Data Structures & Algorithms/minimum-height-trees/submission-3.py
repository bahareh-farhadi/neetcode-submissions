# the brute force approace is O(V(V+E)) or O(n(n+n-1)) which is O(n^2)
# but there is a better way to solve this is O(n).
# The idea is that the nodes in the centre (the non-leave nodes) have the smallest height. Now mathematically there is either 1 or maximum 2 nodes with this behaviour. 
# We start with leaf nodes and remove them from the tree until we have 2 or less than 2 nodes. Then we return those nodes as the centre nodes with smallest height.
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        ad_list=dict()
        for i in range(n):
            ad_list[i]=list()
        for e in edges:
            ad_list[e[0]].append(e[1])
            ad_list[e[1]].append(e[0])
        leaves=deque()
        edge_count=dict()
        for i in range(n):
            if len(ad_list[i])==1:
                # leaf node
                leaves.append(i)
            edge_count[i]=len(ad_list[i])
        
        while len(leaves)>0:
            if n<=2:
                return list(leaves)
            # each time only look at the leaves that were added in the previous iteration (not all leaves)
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for neighbour in ad_list[node]:
                    edge_count[neighbour]-=1
                    if edge_count[neighbour]==1:
                        leaves.append(neighbour)

            
        