# the idea is to build an adjacency list and then use bfs/dfs to go over it. We have to detect a cycle. If we visit a node twice within the same PATH (so not overall, but in each dfs iteration) that means there is a cycle hence it is not possible to finish all courses.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        ad_list=dict()
        for i in range(numCourses):
            ad_list[i]=list()
        for p in prerequisites:
            ad_list[p[0]].append(p[1])
        visited=set() #only adding courses to this set once its full path has been explored
        stack=list()
        for course in ad_list.keys():
            if course not in visited:
                stack.append((course,False)) #False means this course has not started being explored yet
                path=set()
                while len(stack)>0:
                    elem=stack.pop()
                    curr_course=elem[0]
                    status=elem[1]
                    if curr_course in visited:
                        continue
                    if status==True:
                        # all prereqs for this course have been epxlored, so this can be marked as visited and can be removed from the current path
                        path.remove(curr_course)
                        visited.add(curr_course)
                        continue
                    if curr_course in path:
                        # cycle is detected
                        return False
                    path.add(curr_course)
                    stack.append((curr_course, True)) #once all prereqs are popped we get back to this and we can mark it visited since it has True status
                    for p in ad_list[curr_course]:
                        if p not in visited:
                            stack.append((p, False))
        return True
                    
                
    
        