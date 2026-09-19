import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_heap=list()
        i=0
        curr_capacity=0
        while i<len(trips):
            while len(min_heap)>0:
                # if the end location is ending or has ended before the current start location
                if trips[i][1]>=min_heap[0][0]:
                    curr_capacity-=min_heap[0][1]
                    heapq.heappop(min_heap)
                else:
                    break

            
            curr_capacity+=trips[i][0]
            if curr_capacity>capacity:
                return False
            heapq.heappush(min_heap, [trips[i][2], trips[i][0]])
            i+=1
        return True
            
        