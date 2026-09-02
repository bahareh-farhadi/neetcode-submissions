class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        seen=set()
        max_len=0
        while high<len(s):
            if s[high] not in seen:
                seen.add(s[high])
                max_len=max(max_len, high-low+1)
                high+=1
            else:
                seen.remove(s[low])
                low+=1
                if low>high:
                    high+=1
        return max_len


        