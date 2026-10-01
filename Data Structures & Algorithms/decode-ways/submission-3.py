class Solution:
    def numDecodings(self, s: str) -> int:
        s = [int(char) for char in s]
        dp=list()
        for i in range(len(s)+1):
            dp.append(1)
        
        for i in range(len(s)-1, -1, -1):
            if s[i]==0:
                dp[i]=0
                continue

            if i<len(s)-1:
                if s[i]==1 or (s[i]==2 and s[i+1]<=6):
                    dp[i]=dp[i+1]+dp[i+2] # we want to take 2 digits so we add the possibility of the next 2 dp to the current one 
                else:
                    dp[i]=dp[i+1] #since we only are taking the current digit the number of possibilities is the same as next one
            
        return dp[0]
        