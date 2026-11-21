import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        min_heap = list() # ready_time, room_num
        num_meetings = dict()
        for i in range(n):
            heapq.heappush(min_heap, (0, i))
            num_meetings[i] = 0
        
        for meeting in meetings:
            while min_heap[0][0] < meeting[0]:
                ready = heapq.heappop(min_heap)
                ready_room = ready[1]
                ready_time = meeting[0]
                heapq.heappush(min_heap, (ready_time, ready_room))
            ready = heapq.heappop(min_heap)
            start_time = ready[0]
            ready_room = ready[1]
            end_time = start_time + (meeting[1] - meeting[0])
            heapq.heappush(min_heap, (end_time, ready_room))
            num_meetings[ready_room]+=1
        
        res = 0
        max_count = 0
        for key, val in num_meetings.items():
            if val > max_count:
                res = key
                max_count = val
        return res

        