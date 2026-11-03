"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # the idea is that we create 2 lists, start and end. start includes the start time and end includes the end times (all sorted). we use 2 pointers on the 2 arrays. if start[i]<end[j] that means meeting i has to start beofre meeting j will end so we increment the room count. if start[i]==end[j] then meeting j ends and meeting i starts right after, so number of rooms will decrement. if start[i]>end[j] that means we will decrement the room number since meeting j has ended before meeting i started.
        if len(intervals)==0:
            return 0
        start=list()
        end=list()
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        count=0
        rooms_count=0
        i=0
        j=0
        while i<len(start) and j<len(end):
            if start[i]<end[j]:
                count+=1
                rooms_count=max(rooms_count, count)
                i+=1
            elif start[i]>=end[j]:
                count-=1
                j+=1
        return rooms_count
            
                

        