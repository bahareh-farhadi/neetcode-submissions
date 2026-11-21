import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the idea is to schedule tasks with the highest count first since those would be the hardest to fit into the schedule. 
        # we will use max heap to keep track of the highest count jobs, at each time we check if a job is ready (in the heap) or not, if it is ready we pop if off the heap and add it to a cooldown queue until the cooldown time is finished and then we add it back to the heap. we continue this until there are no jobs left
        ready = list() # max heap (count, job)
        cooldown = deque() # (remaining count, task, ready time)
        count = dict()
        for task in tasks:
            if task in count:
                count[task]+=1
            else:
                count[task] = 1
        for key, val in count.items():
            heapq.heappush(ready, (-val, key))
        time = 0
        while ready or cooldown:
            # instead of increasinfg time 1 by 1 we can jumpt to cooldown time if there are no ready tasks
            if not ready:
                item = cooldown.popleft()
                remaining_count = item[0]
                task = item[1]
                time = item[2]
                heapq.heappush(ready, (-remaining_count, task))   
            time+=1
            if ready:
                item = heapq.heappop(ready)
                remaining_count = abs(item[0]) - 1
                if remaining_count > 0:
                    task = item[1]
                    cooldown.append((remaining_count, task, time + n))
            if cooldown and cooldown[0][2] == time:
                item = cooldown.popleft()
                remaining_count = item[0]
                task = item[1]
                heapq.heappush(ready, (-remaining_count, task))
        return time
        
        

        