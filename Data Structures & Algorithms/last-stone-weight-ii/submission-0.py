class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # this is also a 0/1 knapsack question
        # The important idea is that we have to try our best to divide stones into two equal halves such that we get two equal sums so we know the different of the 2 halves is 0. Obviously that is not always possible but we have to see what would be the closest we get to the half and then we do half-closest=difference where difference is the answer. 
        # dp[i][sum]=max(dp[i-1][sum-num]+num, dp[i-1][sum])

        stones.sort()
        total_sum=0
        for stone in stones:
            total_sum+=stone
        half_sum=total_sum//2
        dp=list()
        for i in range(len(stones)+2):
            temp=list()
            for j in range(half_sum+2):
                temp.append(0)
            dp.append(temp)
        
        # first row is the sum
        for j in range(1, len(dp[0])):
            dp[0][j]=j-1
        
        # second row is all 0's
        for j in range(len(dp[0])):
            dp[1][j]=0
        
        # first column is the stones
        k=0
        for i in range(2, len(dp)):
            dp[i][0]=stones[k]
            k+=1

        for i in range(2, len(dp)):
            for j in range(2, len(dp[0])):
                curr_sum=dp[0][j]
                curr_sum_index=curr_sum+1
                stone=dp[i][0]
                if curr_sum_index-stone>=1:
                    dp[i][j]=max(dp[i-1][curr_sum_index-stone]+stone, dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        
        closest_half=dp[-1][-1]
        return abs(total_sum-closest_half*2)
        