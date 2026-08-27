class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        low=0
        high=len(s)-1
        while low<high:
            if s[low].isalnum()==False:
                low+=1
                continue
            if s[high].isalnum()==False:
                high-=1
                continue
            if s[low]!=s[high]:
                return False
            else:
                low+=1
                high-=1
        return True
        