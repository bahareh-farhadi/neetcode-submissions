# can use both dp and two pointer, two pointer has less space complexity but for practice I am going to do dp
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=list()
        for i in range(len(s)):
            temp=list()
            for j in range(len(s)):
                temp.append(False)
            dp.append(temp)

        count=0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                # j-i<=2 is because we are checking whether this is a 1 char, 2 char or 3 char string. if 2 char and the current are equal that means this is like aa, and if 3 char this means this is anything like aba (or even aaa)
                if s[i]==s[j] and (j<=i+2 or dp[i+1][j-1]==True):
                    dp[i][j]=True
                    count+=1
        return count
                    
        