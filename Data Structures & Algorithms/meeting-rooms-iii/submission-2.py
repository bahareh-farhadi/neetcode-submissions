import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # using two heaps - this approach has better time complexity than one min, one min has average O(mlogm + mlogn) but at worst O(mlogm + mn), but two heaps has always O(mlom + mlogn)
        meetings.sort()
        used_rooms = list() # (ready_time, ready_room)
        available_rooms = list() # room number
        room_count = dict()
        for i in range(n):
            heapq.heappush(available_rooms, i)
            room_count[i] = 0
        for meeting in meetings:
            end_time = meeting[1]
            while used_rooms and used_rooms[0][0] <= meeting[0]:
                ready_time, ready_room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, ready_room)
            if not available_rooms:
                ready_time, ready_room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, ready_room)
                # have to jump start time
                end_time = ready_time + (meeting[1] - meeting[0])
            
            ready_room = heapq.heappop(available_rooms)
            heapq.heappush(used_rooms, (end_time, ready_room))
            room_count[ready_room]+=1
        
        res = 0
        max_count = 0
        for key, val in room_count.items():
            if val > max_count:
                max_count = val
                res = key
        return res

            
            
                
