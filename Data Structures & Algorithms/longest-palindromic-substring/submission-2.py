# we use a 2d dp to solve this 
# if dp[i][j] is True then s[i:j+1] is a palindrome
# time O(n^2), space O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=list()
        for i in range(len(s)):
            temp=list()
            for j in range(len(s)):
                temp.append(False)
            dp.append(temp)
        max_len=0
        res=""
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j]=True 
                    
                    if j+1-i > max_len:
                        max_len=j+1-i
                        res=s[i:j+1]
        return res
        
        

            

        