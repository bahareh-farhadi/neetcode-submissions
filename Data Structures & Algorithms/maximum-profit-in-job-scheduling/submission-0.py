class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # the idea is to use dynamic programming to keep track of the max profit + use binary search to find the first non-overlapping interval and add its profit to the current profit
        n = len(startTime)
        dp = [0] * (n+1)
        data = list()
        for i in range(n):
            data.append((startTime[i], endTime[i], profit[i]))
        data.sort()
        for i in range(n-1, -1, -1):
            low = i + 1
            high = n - 1
            potential = None
            while low <= high:
                mid = (low + high) // 2
                if data[i][1] > data[mid][0]:
                    # overlapping
                    low = mid + 1
                else:
                    potential = mid
                    high = mid - 1
            if potential == None:
                # all overlapping
                dp[i] = max(dp[i+1], data[i][2])
            else:
                dp[i] = max(dp[i+1], data[i][2] + dp[potential])
        return dp[0]


        