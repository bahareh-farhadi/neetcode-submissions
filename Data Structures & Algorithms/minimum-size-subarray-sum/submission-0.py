class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float('inf')
        low=0
        high=0
        curr_sum=nums[high]
        while high<len(nums):
            if curr_sum>=target:
                min_len=min(min_len, high-low+1)
                curr_sum-=nums[low]
                low+=1
            else:
                high+=1
                if high<len(nums):
                    curr_sum+=nums[high]
        if min_len==float('inf'):
            return 0
        else:
            return min_len

        