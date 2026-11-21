class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        groups = dict() #key: group, val: list of the nodes
        nodes = dict() # key: node, val: its group
        res = None
        last_group = 0
        for edge in edges:
            if edge[0] in nodes and edge[1] in nodes:
                # need merging if they have different groups, else it can be res
                if nodes[edge[0]] != nodes[edge[1]]:
                    # merge
                    staying_group = nodes[edge[0]]
                    deleting_group = nodes[edge[1]]
                    for changing_node in groups[deleting_group]:
                        nodes[changing_node] = staying_group
                        groups[staying_group].append(changing_node)
                    del groups[deleting_group]
                else:
                    res = edge
            else:
                if edge[0] in nodes:
                    group = nodes[edge[0]]
                    nodes[edge[1]] = group
                    groups[group].append(edge[1])
                elif edge[1] in nodes:
                    group = nodes[edge[1]]
                    nodes[edge[0]] = group
                    groups[group].append(edge[0])
                else:
                    last_group+=1
                    groups[last_group] = list()
                    groups[last_group].append(edge[0])
                    groups[last_group].append(edge[1])
                    nodes[edge[0]] = last_group
                    nodes[edge[1]] = last_group
        return res
