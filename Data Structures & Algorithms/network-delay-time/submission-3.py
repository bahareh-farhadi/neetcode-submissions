import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we use dijsktra algorithm to solve this
        # the idea is to use BFS but instead of a queue we use a min heap where elements are (dist, node) so we visit smaller distances untill all nodes have been visisted

        ad_list = dict()
        for i in range(1, n+1):
            ad_list[i] = list()
        
        for t in times:
            first_node = t[0]
            second_node = t[1]
            distance = t[2]
            ad_list[first_node].append((second_node, distance))
        visited = set()
        min_heap = list()
        visited.add(k)
        for item in ad_list[k]:
            heapq.heappush(min_heap, (item[1], item[0]))
        max_dist = 0
        while min_heap:
            elem = heapq.heappop(min_heap)
            dist = elem[0]
            dest = elem[1]
            if dest in visited:
                continue
            max_dist = max(max_dist, dist)
            
            visited.add(dest)
            if len(visited) == n:
                break
            for item in ad_list[dest]:
                if item[0] not in visited:
                    heapq.heappush(min_heap, (item[1] + dist, item[0]))
        
        if len(visited) < n:
            return -1
        return max_dist


        