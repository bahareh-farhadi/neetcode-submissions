# space optimized version
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        first=nums[0]
        second=max(nums[0], nums[1])
        if len(nums)==2:
            return max(first, second)
        for i in range(2, len(nums)):
            third=max(nums[i]+first, second)
            first=second
            second=third
        return max(second, third)
        