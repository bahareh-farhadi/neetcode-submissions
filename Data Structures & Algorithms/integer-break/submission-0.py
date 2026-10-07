class Solution:
    def integerBreak(self, n: int) -> int:
        dp=list()
        for i in range(n+1):
            dp.append(0)
        dp[1]=1
        for i in range(2, n+1):
            if i==n:
                dp[i]=0
            else:
                dp[i]=i # this is because we want to make sure the next number e.g. if current is 4 and the next is 5, so 5=4+1 gets dp[1]*dp[4]. obviously this can't be applied to the last number since we have to return actual results.
            for j in range(1, i):
                dp[i]=max(dp[i], dp[j]*dp[i-j])
        return dp[-1]
        