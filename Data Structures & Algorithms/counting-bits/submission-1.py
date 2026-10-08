class Solution:
    def countBits(self, n: int) -> List[int]:
        # combine using dp 
        # we know numbers only have 1 set bit at powers of 2
        # so every number would be  dp[num]=1+dp[num-biggest power of 2 number]
        dp=list()
        for i in range(n+1):
            dp.append(0)
        if n==0:
            return dp
        dp[1]=1
        last_power_2=1
        for i in range(2, n+1):
            if last_power_2*2==i:
                last_power_2=i
                dp[i]=1
            else:
                dp[i]=1+dp[i-last_power_2]
        return dp
        