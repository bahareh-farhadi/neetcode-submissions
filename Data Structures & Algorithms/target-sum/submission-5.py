class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # this is the 0/1 knapsack question, since we can either "add" or "subtract" (we have 2 possibilities)
        # we consider all possible sums for the numbers, e.g. for 2,2,2 possible sums are from -6 to 6. Then for each item we will have dp[current_sum-num]+dp[current_sum+num] (e.g. sum of 0 with [2,2] is basically sum of 2 added 2 and 2 subtract 2.)
        dp=list()
        least_sum=0
        greatest_sum=0
        for num in nums:
            greatest_sum+=num
        least_sum=-greatest_sum
        for i in range(len(nums)+2): 
            temp=list()
            for j in range(greatest_sum-least_sum+2):
                temp.append(0)
            dp.append(temp)
        # first row
        for j in range(1, len(dp[0])):
            dp[0][j]=least_sum
            least_sum+=1
        
        # first column - second row is initialized to 0
        dp[1][0]=0
        # initialize row for 0
        for j in range(1, len(dp[0])):
            if dp[0][j]==0:
                dp[1][j]=1
            else:
                dp[1][j]=0
        k=0
        for i in range(2, len(dp)):
            dp[i][0]=nums[k]
            k+=1
        
        for i in range(2, len(dp)):
            for j in range(1, len(dp[0])):
                # dp[0][j] is the sum
                if 1<=dp[0][j]-dp[i][0]+greatest_sum+1<len(dp[0]):
                    dp[i][j]+=dp[i-1][dp[0][j]-dp[i][0]+greatest_sum+1]
                if 1<=dp[0][j]+dp[i][0]+greatest_sum+1<len(dp[0]):
                    dp[i][j]+=dp[i-1][dp[0][j]+dp[i][0]+greatest_sum+1]
        for j in range(1, len(dp[0])):
            if dp[0][j]==target:
                return dp[-1][j]
        return 0
            

                
        