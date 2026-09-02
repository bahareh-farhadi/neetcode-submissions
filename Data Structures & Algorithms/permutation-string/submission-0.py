class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_pattern=list()
        s2_pattern=list()
        for i in range(26):
            s1_pattern.append(0)
            s2_pattern.append(0)
        for char in s1:
            s1_pattern[ord(char)-ord('a')]+=1
        print(s1_pattern)
        low=0
        high=len(s1)-1
        for i in range(low, high+1):
            s2_pattern[ord(s2[i])-ord('a')]+=1
        while high<len(s2):
            if s1_pattern==s2_pattern:
                return True
            else:
                s2_pattern[ord(s2[low])-ord('a')]-=1
                low+=1
                high+=1
                if high<len(s2):
                    s2_pattern[ord(s2[high])-ord('a')]+=1
        return False