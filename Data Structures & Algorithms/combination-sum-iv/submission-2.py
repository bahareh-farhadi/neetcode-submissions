class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=list()
        nums.sort()
        for i in range(target+1):
            dp.append(0)
        for num in nums:
            if num>len(dp)-1:
                break
            dp[num]=1
        for i in range(1, target+1):
            for num in nums:
                if num>i:
                    break
                dp[i]+=dp[i-num]
        return dp[-1]

        