class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ad_list = dict() # key: node, val: list of connected nodes
        for i in range(n):
            ad_list[i] = list()
        for edge in edges:
            ad_list[edge[0]].append(edge[1])
            ad_list[edge[1]].append(edge[0])
        stack = list()
        visited = set()
        stack.append((0, None))
        visited.add(0)
        while stack:
            node, parent = stack.pop()
            for nei in ad_list[node]:
                if nei in visited and nei != parent:
                    # cycle
                    return False
                elif nei not in visited and nei != parent:
                    stack.append((nei, node))
                    visited.add(nei)
        if len(visited) == n:
            return True
        else:
            return False
        

        