class Solution:
    def numSquares(self, n: int) -> int:
        sq_num=list()
        dp=list()
        for i in range(n+1):
            dp.append(float('inf'))
        dp[0]=0
        dp[1]=1
        sq_num.append(1)
        for i in range(2, n+1):
            if ((sq_num[-1]**0.5)+1)**2==i:
                sq_num.append(((sq_num[-1]**0.5)+1)**2)
                dp[i]=1
            else:
                for j in sq_num:
                    dp[i]=min(dp[i], int(i/j)+dp[int(i%j)])
        return dp[-1]
        