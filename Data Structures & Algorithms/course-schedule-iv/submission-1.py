class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # dfs + hashset
        # do a dfs for each query, and add all reachable nodes for the starting node
        ad_list=dict()
        for i in range(numCourses):
            ad_list[i]=list()
        for p in prerequisites:
            ad_list[p[0]].append(p[1])
        reachable=dict()
        res=list()
        for q in queries:
            first_node=q[0]
            second_node=q[1]
            if first_node in reachable and second_node in reachable[first_node]:
                res.append(True)
                continue
            visited=set()
            stack=list()
            stack.append(first_node)
            while len(stack)>0:
                elem=stack.pop()
                if elem in visited:
                    continue
                visited.add(elem)
                if first_node not in reachable:
                    reachable[first_node]=set()
                val=ad_list[elem]
                for item in val:
                    reachable[first_node].add(item)
                    if item not in visited:
                        stack.append(item)
            if first_node in reachable and second_node in reachable[first_node]:
                res.append(True)
            else:
                res.append(False)
        return res
        
                
                    


        