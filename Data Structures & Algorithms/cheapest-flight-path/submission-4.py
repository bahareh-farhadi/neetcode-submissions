import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ad_list = dict()
        for i in range(n):
            ad_list[i] = list()
        
        for f in flights:
            first_node = f[0]
            second_node = f[1]
            cost = f[2]
            ad_list[first_node].append((second_node, cost))
        
        visited = set()
        min_heap = list()
        for item in ad_list[src]:
            if item[0] == dst:
                num_stops = 0
            else:
                num_stops = 1
            heapq.heappush(min_heap, (num_stops, item[1], item[0]))

        visited.add((src, 0))
        min_cost = float('inf')
        while min_heap:
            elem = heapq.heappop(min_heap)
            cost = elem[1]
            num_stops = elem[0]
            dest = elem[2]
            if num_stops > k:
                continue
            if dest == dst and num_stops <= k:
                min_cost = min(min_cost, cost)
            if (dest, num_stops) in visited:
                continue
            visited.add((dest, num_stops))
            for item in ad_list[dest]:
                if item[0] == dst:
                        heapq.heappush(min_heap, (num_stops, item[1] + cost, item[0]))
                else:
                        heapq.heappush(min_heap, (num_stops + 1, item[1] + cost, item[0]))
        if min_cost == float('inf'):
            return -1
        else:
            return min_cost



        