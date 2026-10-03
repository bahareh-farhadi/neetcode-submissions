class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # use a min and max values + a global max
        # initially set both min and max to the first value
        # 1- if num*min>num*max swap min and max
        # 2- if num*min < min then min=num*min else min=num
        # 3- if num*max > max then max=num*max else max=num
        res=nums[0]
        min_num=nums[0]
        max_num=nums[0]
        for i in range(1, len(nums)):
            if nums[i]*min_num>nums[i]*max_num:
                min_num, max_num = max_num, min_num
            min_num=min(nums[i]*min_num, nums[i])
            max_num=max(nums[i]*max_num, nums[i])
            res=max(res, max_num)
        return res
        