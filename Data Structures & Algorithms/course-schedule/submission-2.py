from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = dict() # key: prereq, val: list of courses that have to be taken after key
        num_prereqs = dict() # key: course, val: numbers of prereqs that have not been taken yet
        for i in range(numCourses):
            courses[i] = list()
            num_prereqs[i] = 0
        
        for prereq, course in prerequisites:
            courses[prereq].append(course)
            num_prereqs[course] += 1

        queue = deque()
        for i in range(numCourses):
            if num_prereqs[i] == 0:
                queue.append(i)
        if len(queue) == 0:
            # no courses with no prereqs
            return False
        
        while queue:
            course = queue.popleft()
            for next_course in courses[course]:
                if num_prereqs[next_course] > 0:
                    num_prereqs[next_course] -= 1
                    if num_prereqs[next_course] == 0:
                        queue.append(next_course)
        for course, num in num_prereqs.items():
            if num > 0:
                return False
        return True

                
        
        