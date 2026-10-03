class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=list()
        for num in nums:
            dp.append(1)
        max_len=1
        for i in range(len(nums)-2, -1, -1):
            curr_len=0
            for j in range(i+1, len(nums)):
                if nums[j]>nums[i] and dp[j]>curr_len:
                    curr_len=dp[j]
                    dp[i]=dp[j]+1
            max_len=max(max_len, dp[i])
        return max_len
        