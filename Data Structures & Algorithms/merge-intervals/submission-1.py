class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res=list()
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            greatest_end=res[-1][1]
            
            if intervals[i][0]<=greatest_end:
                greatest_end=max(greatest_end, intervals[i][1])
                res[-1][1]=greatest_end
            else:
                res.append(intervals[i])
        return res

        