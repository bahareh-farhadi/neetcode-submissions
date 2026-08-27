class Solution:
    def check(self, s):
        low=0
        high=len(s)-1
        while low<high:
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        low=0
        high=len(s)-1
        while low<high:
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                return self.check(s[low+1:high+1]) or self.check( s[low:high])
        return True

        