class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # the idea is to see if there is an overlap and then remove the interval that ends later since that prevents it overlapping with more intervals that come later
        res=0
        intervals.sort(key=lambda x: x[0])
        prev_end=intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end>intervals[i][0]:
                prev_end=min(prev_end, intervals[i][1])
                res+=1
            else:
                # no overlap
                prev_end=intervals[i][1]
        return res
                

        