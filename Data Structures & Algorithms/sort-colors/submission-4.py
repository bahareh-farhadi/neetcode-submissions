class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        curr=0
        while left<right and curr<=right:
            if nums[curr]==0:
                nums[curr]=nums[left]
                nums[left]=0
                left+=1
                curr+=1
            elif nums[curr]==2:
                nums[curr]=nums[right]
                nums[right]=2
                right-=1
            else:
                curr+=1
        return nums
        