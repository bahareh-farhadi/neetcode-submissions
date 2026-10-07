class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=list()
        for i in range(m):
            temp=list()
            for j in range(n):
                temp.append(float('inf'))
            dp.append(temp)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                
        return dp[-1][-1]
            
        