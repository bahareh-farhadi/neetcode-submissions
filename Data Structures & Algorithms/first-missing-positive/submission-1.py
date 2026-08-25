class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # the idea is to use nums itself as a hashset
        # 1. modify all negative values to 0 since we don't care about them
        # 2. whenever we see a positive value we mark that value at its index to a negative value, e.g. 3, 0, 3, 6 in this array we have 3 whose index will be 2 so we change the array to 3, 0, -3, 6. then we start from the beginning of the array and as soon as we see a positive number we know that it is missing. here 3 at index 0 is positive so number 1 is missing.
        
        # convert invalid values (<=0 or >len(nums)) to a safe placeholder
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        # mark as negative
        for i in range(len(nums)):
            if abs(nums[i])-1>=0 and abs(nums[i])-1<len(nums):
                nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
        print(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                return i+1
        return len(nums)+1
        