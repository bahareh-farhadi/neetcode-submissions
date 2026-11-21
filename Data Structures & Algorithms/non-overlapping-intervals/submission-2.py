class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = None
        for interval in intervals:
            if prev is not None:
                if prev > interval[0]:
                    prev = min(prev, interval[1])
                    res+=1
                else:
                    prev = max(prev, interval[1])
            else:
                prev = interval[1]
        return res
        