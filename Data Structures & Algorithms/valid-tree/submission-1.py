# The idea is to do a basic dfs with a small twist. We have to keep track of the parent of every node, so when we encounter a neighbour node that has been visisted and is NOT the parent then we know there is a cycle. 
# at the end we have to check the number of nodes in the visited set to see if all nodes can be reachable from the first node (fully connected).
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited=set()
        ad_list=dict()
        for i in range(n):
            ad_list[i]=list()
        for e in edges:
            ad_list[e[0]].append(e[1])
            ad_list[e[1]].append(e[0])
            
        stack=list()
        # assume all graphs have a node 0 who doesn't have a parent
        stack.append((0,-1))
        visited.add(0)
        while len(stack)>0:
            elem=stack.pop()
            node=elem[0]
            parent=elem[1]
            for neighbour in ad_list[node]:
                if neighbour not in visited:
                    stack.append((neighbour, node))
                    visited.add(neighbour)
                else:
                    # if parent that is ok
                    if neighbour==parent:
                        continue
                    else:
                        return False
        if len(visited)==n:
            return True
        else:
            return False
                    
                    


        

        