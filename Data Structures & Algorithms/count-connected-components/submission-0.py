class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ad_list=dict()
        for i in range(n):
            ad_list[i]=list()
        for e in edges:
            ad_list[e[0]].append(e[1])
            ad_list[e[1]].append(e[0])
        visited=set()
        count=0
        for key in ad_list.keys():
            if key in visited:
                continue
            stack=list()
            stack.append(key)
            count+=1
            while len(stack)>0:
                node=stack.pop()
                visited.add(node)
                for item in ad_list[node]:
                    if item not in visited:
                        stack.append(item)
        return count
        