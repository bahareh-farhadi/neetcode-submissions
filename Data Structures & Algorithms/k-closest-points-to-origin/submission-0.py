import heapq
class Solution:
    def calc_distance(self, x, y):
        return (x**2+y**2)**0.5
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap=list()
        for point in points:
            d=self.calc_distance(point[0], point[1])
            heapq.heappush(min_heap, [d, point[0], point[1]])
        res=list()
        for i in range(k):
            [d, point[0], point[1]]=heapq.heappop(min_heap)
            res.append([point[0], point[1]])
        return res
            

        