class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = list()
        for interval in intervals:
            if len(res) > 0 and res[-1][1] >= interval[0]:
                # merge
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
            prev = res[-1][1]
        return res
        