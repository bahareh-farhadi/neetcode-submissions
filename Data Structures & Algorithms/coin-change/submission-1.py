# Bottom-up approach
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=dict()
        dp[0]=0
        for i in range(1, amount+1):
            dp[i]=float('inf')
        for i in range(1, amount+1):
            for coin in coins:
                if i<coin:
                    continue
                
                dp[i]=min(dp[i], 1+dp[i-coin])
        if dp[amount]==float('inf'):
            return -1
        else:
            return dp[amount]