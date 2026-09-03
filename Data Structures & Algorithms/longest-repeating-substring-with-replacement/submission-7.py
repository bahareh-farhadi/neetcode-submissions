class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The idea is to use a sliding window
        # for every window we keep track of the frequency of each character seen. We want to see what "less" frequent characters need to be replaced so that the number of replacements is less than or equal to k. Once the number of replacements increase k we shrink the window
        seen=dict()
        low=0
        high=0
        max_freq=0
        max_len=0
        while high<len(s):
            if s[high] not in seen:
                seen[s[high]]=1
            else:
                seen[s[high]]+=1
            if seen[s[high]]>max_freq:
                max_freq=seen[s[high]]
            window_len=high-low+1
            if window_len-max_freq<=k:
                max_len=max(max_len, window_len)
                high+=1
            else:
                while low<=high:
                    seen[s[low]]-=1
                    max_freq=0
                    for val in seen.values():
                        max_freq=max(max_freq, val)
                    if seen[s[low]]==0:
                        del seen[s[low]]
                    low+=1
                    window_len=high-low+1
                    if window_len-max_freq<=k:
                        break
                high+=1
                    
        return max_len

        