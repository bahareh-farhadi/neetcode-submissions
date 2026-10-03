# Top-Bottom approach
import math
class Solution:
    dp=dict()
    def helper(self, coins, amount):
        if amount==0:
            #Solution.dp[amount]=count
            return 0
        if amount in Solution.dp:
            return Solution.dp[amount]
        curr_count=float('inf')
        for coin in coins:
            if amount<coin:
                continue
            if amount-coin in Solution.dp:
                curr_count=min(curr_count, 1+Solution.dp[amount-coin])
            else:
                coin_count=self.helper(coins, amount-coin)
                curr_count=min(curr_count, 1+coin_count)
        Solution.dp[amount]=curr_count
        return curr_count

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        Solution.dp.clear()
        self.helper(coins, amount)
        min_count=Solution.dp[amount]
        if min_count==float('inf'):
            return -1
        return min_count
        