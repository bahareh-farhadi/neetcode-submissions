class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list()
        t_list=list()
        for i in range(26):
            s_list.append(0)
            t_list.append(0)
        for i in range(len(s)):
            s_list[ord(s[i])-ord('a')]+=1
        for j in range(len(t)):
            t_list[ord(t[j])-ord('a')]+=1
        for i in range(26):
            if s_list[i]!=t_list[i]:
                return False
        return True
        
        