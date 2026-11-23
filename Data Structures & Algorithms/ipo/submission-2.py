import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        data = list()
        for i in range(len(profits)):
            data.append((capital[i], profits[i]))
        data.sort()
        j = 0
        max_heap = list() # profits get added here
        i = 0
        while i < k and j < len(data):
            while j < len(data) and data[j][0] <= w:
                heapq.heappush(max_heap, -data[j][1])
                j+=1
            if max_heap:
                profit = abs(heapq.heappop(max_heap))
                w+=profit
            i+=1
        while i < k and max_heap:
            w+=abs(heapq.heappop(max_heap))
            i+=1
        return w

            

        