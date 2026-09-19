import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        total=w
        p=list()
        for i in range(len(profits)):
            p.append([profits[i], capital[i]])
        p.sort(key=lambda x: x[1])
        max_heap=list()
        i=0
        while k>0:
            while i<len(p) and total>=p[i][1]:
                heapq.heappush(max_heap, [-p[i][0], -p[i][1]])
                i+=1
            if len(max_heap)>0:
                elem=heapq.heappop(max_heap)
                total+=-elem[0]
                k-=1
            else:
                break
        return total
        