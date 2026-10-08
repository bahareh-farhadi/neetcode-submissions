class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # we will use a 2d dp to solve this
        # our col will be 0 to amount and our rows will be coins (sorted from highest to lowest)
        # we initiliaze amount 0 for all coins to be 1 (1 way to get 0 amount)
        # then for each amount we do dp[i][j]=dp[i][amount-coin]+dp[i-1][j]
        # dp[amount-coin] is basically the amount for not having coin, e.g. dp[4] for coin 2 can be the same as dp[4-2]=dp[2] at minimum. e.g. for amount 2 we have (1,1) and (2) so adding a 2 coin we will have (1,1,2) and (2,2) so the same combinations just add 2 coin to each.
        # dp[i-1][j] is the number of combinations for the same amount but with the previous coin, so we add up all those combinations as well.

        dp=list()
        coins.sort()
        for i in range(len(coins)+1):
            temp=list()
            for j in range(amount+2):
                temp.append(0)
            dp.append(temp)
        coins_copy=coins.copy()
        for i in range(len(coins)+1):
            for j in range(amount+2):
                if i==0 and j>0:
                    # first row is amounts
                    dp[i][j]=j-1
                elif j==0 and i>0:
                    # first col is the coins
                    dp[i][j]=coins_copy.pop()
                elif j==1:
                    # possibility for amount 0
                    dp[i][j]=1

        for j in range(2, amount+2):
            for i in range(1, len(coins)+1):
                
                if dp[0][j]<dp[i][0]:
                    # if amount<coin:
                    dp[i][j]=0
                else:
                    coin=dp[i][0]
                    curr_amount=dp[0][j]
                    if i>=2:
                        dp[i][j]=dp[i][curr_amount-coin+1]+dp[i-1][j]
                    else:
                        dp[i][j]=dp[i][curr_amount-coin+1]
        return dp[-1][-1]

                
                
        

        