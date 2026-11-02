# create a new output list, it will be less time complexity 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=list()
        if len(intervals)==0:
            return [newInterval]
        i=0
        # add all intervals less than the new interval
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        # add all the overlapping intervals
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval=[min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i+=1
        # add the new interval
        res.append(newInterval)

        # add all the intervals that start after the new interval
        while i<len(intervals):
            res.append(intervals[i])
            i+=1
        return res

                
                    
       
        