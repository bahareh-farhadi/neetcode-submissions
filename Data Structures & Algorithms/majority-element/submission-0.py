class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i+len(nums)//2]==nums[i]:
                return nums[i]
        