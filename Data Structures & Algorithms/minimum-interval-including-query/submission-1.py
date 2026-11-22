import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # the idea is to use min_heap (store (length, end_time)). we iterate through the queries and the intervals, if query > end_time then keep poppin elements off the heap, else keep adding intervals to the heap until start <= query <= end
        query_map = dict()
        q_copy = list(set(queries.copy()))
        q_copy.sort()
        
        intervals.sort()
        i = 0 # pointer for queries
        j = 0 # pointer for intervals
        min_heap = list()
        while i < len(q_copy):
            while len(min_heap) > 0 and  min_heap[0][1] < q_copy[i]:
                heapq.heappop(min_heap)
            while j < len(intervals):
                if intervals[j][0] <= q_copy[i] <= intervals[j][1]:
                    heapq.heappush(min_heap, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                    j+=1
                elif intervals[j][1] < q_copy[i]:
                    j+=1
                else:
                    break
            if min_heap:
                query_map[q_copy[i]] = min_heap[0][0]
            else:
                query_map[q_copy[i]] = -1
            i+=1
        res = list()
        for q in queries:
            res.append(query_map[q])
        return res
                
            

                    
            
