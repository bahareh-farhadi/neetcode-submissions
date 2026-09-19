import heapq
class MedianFinder:

    def __init__(self):
        self.total=0
        self.min_heap=list() #right
        self.max_heap=list() #left
        

    def addNum(self, num: int) -> None:
        if self.total%2==0:
            # have to add to left
            if len(self.min_heap)>0 and num>self.min_heap[0]:
                # swap
                min_heap_top=heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_heap_top)
                # add new element
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            # have to add to right
            if len(self.max_heap)>0 and num<-self.max_heap[0]:
                # swap
                max_heap_top=-heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, max_heap_top)
                # add new element
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        self.total+=1
        

    def findMedian(self) -> float:
        if len(self.min_heap)==0 and len(self.max_heap)==0:
            return 0
        if self.total%2==0:
            return (self.min_heap[0]-self.max_heap[0])/2
        else:
            if len(self.max_heap)>len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]


    
        
        