class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        low=0
        high=1
        profit=0
        while high<len(prices):
            if prices[high]>prices[low]:
                profit=max(profit, prices[high]-prices[low])
                high+=1
            else:
                low=high
                high+=1
        return profit
        