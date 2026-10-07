# the idea is that for each elements we have to see what would be the result of max between stone[i]-dp[i+1] vs. stone[i]+stone[i+1]-dp[i+2] vs. stone[i]+stone[i+1]+stone[i+2]-dp[i+3]. And here dp[i+3] indicates the amount the opponent can take that is why we have to subtract it. 
# we start with a dp array of length n+1 where the last element is 0 (meaning if we started grabbing stone at the nth elements then the n+1th element is 0 meaning nothing is left for the opponent)
# we assume we are Alice and the opponent is Bob; if at the end dp[0] is positive that means Alice wins and if it is negative Bob wins, and if it is 0 then it is a tie.
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp=list()
        for i in range(len(stoneValue)+1):
            dp.append(-float('inf'))
        dp[-1]=0
        for i in range(len(stoneValue)-1, -1, -1):
            if i+3<len(dp):
                dp[i]=max(stoneValue[i]-dp[i+1],
                      stoneValue[i]+stoneValue[i+1]-dp[i+2],
                      stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dp[i+3])
            elif i+2<len(dp):
                dp[i]=max(stoneValue[i]-dp[i+1],
                      stoneValue[i]+stoneValue[i+1]-dp[i+2])
            elif i+1<len(dp):
                dp[i]=stoneValue[i]-dp[i+1]
        
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        else:
            return "Tie"
        
        
            
        