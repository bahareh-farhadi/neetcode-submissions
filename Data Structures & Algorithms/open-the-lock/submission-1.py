# since we are looking for "minimum total number" we have to use bfs
# the idea is to think of each lock combination as a node in a graph. once we visit the node that matches the target we can return. We can use a queue to keep track of (combination, turn_count). For each combination we append the 8 neighbor combinations that come from it (each wheel can turn up or down each time)
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen=set()
        # add the deadends to the seen set so they are not used
        for d in deadends:
            seen.add(d)
        queue=deque()
        if "0000" not in seen:
            queue.append(("0000", 0))
            seen.add("0000")
        
        while len(queue)>0:
            elem=queue.popleft()
            comb=elem[0]
            turn_count=elem[1]
            if comb==target:
                return turn_count
            for i in range(4):
                turn_up=str((int(comb[i])+1)%10)
                neighbor_comb=comb[:i]+turn_up+comb[i+1:]
                if neighbor_comb not in seen:
                    queue.append((neighbor_comb, turn_count+1))
                    seen.add(neighbor_comb)
                turn_down=str((int(comb[i])-1)%10)
                neighbor_comb=comb[:i]+turn_down+comb[i+1:]
                if neighbor_comb not in seen:
                    queue.append((neighbor_comb, turn_count+1))
                    seen.add(neighbor_comb)
        return -1
        