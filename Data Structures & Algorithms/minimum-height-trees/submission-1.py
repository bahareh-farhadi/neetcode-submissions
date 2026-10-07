from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ad_list=dict()
        for i in range(n):
            ad_list[i]=list()
        for e in edges:
            ad_list[e[0]].append(e[1])
            ad_list[e[1]].append(e[0])

        height_dict=dict()
        min_height=float('inf')
        for i in range(n):
            visited=set()
            queue=deque()
            queue.append((i, 0))
            height=0
            curr_height=height
            while len(queue)>0:
                elem=queue.popleft()
                node=elem[0]
                height=elem[1]
                curr_height=max(curr_height, height)
                visited.add(node)
                has_neighbour=False
                for neighbour in ad_list[node]:
                    if neighbour not in visited:
                        has_neighbour=True
                        queue.append((neighbour, height+1))
            
            min_height=min(min_height, curr_height)
            height_dict[i]=curr_height
        
        res=list()
        for key, val in height_dict.items():
            if val==min_height:
                res.append(key)
        return res
            

            

        