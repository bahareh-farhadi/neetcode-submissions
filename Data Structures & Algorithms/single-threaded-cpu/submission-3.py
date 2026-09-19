import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        temp=list()
        for i in range(len(tasks)):
            temp.append([tasks[i][1], i, tasks[i][0]])
        tasks=sorted(temp, key=lambda x: x[2])
        res=list()
        curr=1
        i=0
        #print(tasks)
        min_heap=list()
        # processing, index, enque
        
        while i<len(tasks):
            if tasks[i][2]>curr:
                curr=tasks[i][2]
            else:
                while i<len(tasks) and tasks[i][2]<=curr:
                    heapq.heappush(min_heap, tasks[i])
                    i+=1
                #while len(min_heap)>0:
            if len(min_heap)>0:
                res.append(min_heap[0][1])
                curr+=min_heap[0][0]
                heapq.heappop(min_heap)
        while len(min_heap)>0:
            res.append(min_heap[0][1])
            curr+=min_heap[0][0]
            heapq.heappop(min_heap)

        return res
        
        
                

    

        