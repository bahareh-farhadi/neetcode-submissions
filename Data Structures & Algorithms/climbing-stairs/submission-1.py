class Solution:
    def climbStairs(self, n: int) -> int:
        dp=list()
        dp.append(0)
        dp.append(1) #dp[1]
        dp.append(2)
        for i in range(3, n+1):
            dp.append(0)
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
