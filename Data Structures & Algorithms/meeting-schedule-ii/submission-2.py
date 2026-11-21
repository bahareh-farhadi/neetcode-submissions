"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = list()
        end_times = list()
        for interval in intervals:
            start_times.append(interval.start)
            end_times.append(interval.end)
        start_times.sort()
        end_times.sort()
        i = 0
        j = 0
        count = 0
        res = 0
        while i < len(start_times) and j < len(end_times):
            if start_times[i] < end_times[j]:
                count+=1
                res = max(res, count)
                i+=1
            else:
                count-=1
                j+=1
        return res


        