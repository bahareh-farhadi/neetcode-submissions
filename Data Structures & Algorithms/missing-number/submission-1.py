class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # the bitwise manipulation version
        # we know numbers are 0, 1, ..., n where n is the length of the array
        # and we know we have all numbers besides 1 number in that list
        # so if we xor all the indices with all the numbers we should get a bunch of duplicates and one single index whose number is missing. (order of xoring doesn't matter)
        xor=len(nums)
        for i in range(len(nums)):
            xor=xor^i^nums[i]
        
        return xor
        