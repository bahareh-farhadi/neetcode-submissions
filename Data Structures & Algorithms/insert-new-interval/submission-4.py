class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = list()
        if len(intervals) == 0:
            return [newInterval]
        # parse all smaller intervals
        i = 0
        prev = None
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            new_intervals.append(intervals[i])
            prev = intervals[i][1]
            i+=1

        # add new interval + merge with before if needed
        if prev is not None and prev >= newInterval[0]:
            new_intervals[-1][1] = max(prev, newInterval[1])
        else:
            new_intervals.append(newInterval)
        prev = new_intervals[-1][1]
        
        # add the remaining intervals
        while i < len(intervals):
            if prev >= intervals[i][0]:
                # have to merge
                new_intervals[-1][1] = max(prev, intervals[i][1])
            else:
                new_intervals.append(intervals[i])
            
            prev = new_intervals[-1][1]
            i+=1
        return new_intervals
                
                

        