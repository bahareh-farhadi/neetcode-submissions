class Solution:
    def compare(self, s_seen, t_seen):
        for key, val in t_seen.items():
            if key not in s_seen:
                return False
            else:
                if s_seen[key]<val:
                    return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        t_seen=dict()
        for char in t:
            if char in t_seen:
                t_seen[char]+=1
            else:
                t_seen[char]=1
        low=0
        high=0
        min_len=float('inf')
        res_low=-1
        res_high=-1
        s_seen=dict()
        while high<len(s):
            if s[high] not in t_seen:
                if len(s_seen)>0:
                    high+=1
                else:
                    low+=1
                    high+=1
            else:
                if s[high] not in s_seen:
                    s_seen[s[high]]=1
                else:
                    s_seen[s[high]]+=1
                while self.compare(s_seen, t_seen):
                    window_len=high-low+1
                    if window_len<min_len:
                        min_len=window_len
                        res_low=low
                        res_high=high
                    if s[low] in s_seen:
                        s_seen[s[low]]-=1
                        if s_seen[s[low]]==0:
                            del s_seen[s[low]]
                    low+=1   
                high+=1
        res=s[res_low:res_high+1]
        return res

        