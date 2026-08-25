class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy algorithm solution
        # If today's price is higher than yesterday's price, add the difference to profit
        # this works because buying at 1, holding through 3, 5, and selling at 6 gives the same profit as buying at 1, selling at 3, buying at 3, selling at 5, buying at 5, and selling at 6. (additions and subtractions cancel each other out)
        profit=0
        if len(prices)==1:
            return profit
        for i in range(1, len(prices)):
            diff=prices[i]-prices[i-1]
            if diff>0:
                profit+=diff
        return profit
        
        
        
        