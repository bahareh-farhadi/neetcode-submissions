class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []
        freq_map = dict()
        for i in range(len(s)):
            if s[i] in freq_map:
                freq_map[s[i]][1] = i
            else:
                freq_map[s[i]] = [i, i]
        
        intervals = sorted(list(freq_map.values()))
        
        merged = list()
        merged.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if merged[-1][1] > intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        
        res = list()
        for start, end in merged:
            res.append(end-start+1)
        return res
            
        