# this is similar to Course Schedule I. However, for this question we need to preserve the order of visited nodes. Instead of using a set, we can use a dict since key order is preserved in a dict.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=dict()
        ad_list=dict()
        for i in range(numCourses):
            ad_list[i]=list()
        for p in prerequisites:
            ad_list[p[0]].append(p[1])
        stack=list()
        for course in ad_list:
            if course not in visited:
                stack.append((course, False))
                path=set()
                while len(stack)>0:
                    elem=stack.pop()
                    curr_course=elem[0]
                    status=elem[1]
                    if curr_course in visited:
                        continue
                    if status==True:
                        # end of path, can be removed from path and added to visited
                        path.remove(curr_course)
                        visited[curr_course]=True
                        continue
                    if curr_course in path:
                        #cycle, cannot take these course
                        return []
                    path.add(curr_course)
                    stack.append((curr_course, True))
                    for p in ad_list[curr_course]:
                        if p not in visited:
                            stack.append((p, False))
        for i in range(numCourses):
            if i not in visited:
                visited[i]=True
        return list(visited.keys())
            
        