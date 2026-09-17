import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=list()
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        while len(max_heap)>0:
            x=-(heapq.heappop(max_heap))
            if len(max_heap)>0:
                y=-(heapq.heappop(max_heap))
                if x==y:
                    x=0
                else:
                    heapq.heappush(max_heap, -abs(x-y))
        return x
        