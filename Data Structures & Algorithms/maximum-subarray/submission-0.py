class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''Kadane’s Algorithm is based on one simple observation:
            if the running sum becomes negative, keeping it will only    reduce the sum of any future subarray
So whenever the current sum drops below zero, we reset it and start a new subarray from the next element.'''
        curr_sum=0
        max_sum=nums[0]
        for num in nums:
            if curr_sum<0:
                #reset
                curr_sum=0
            curr_sum+=num
            max_sum=max(max_sum, curr_sum)
        return max_sum
        