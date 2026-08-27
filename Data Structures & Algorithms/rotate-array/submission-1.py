class Solution:
    def helper(self, nums):
        low=0
        high=len(nums)-1
        while low<high:
            nums[low], nums[high] = nums[high], nums[low]
            low+=1
            high-=1
        return nums
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums=self.helper(nums)
        nums[:k]=self.helper(nums[:k])
        nums[k:]=self.helper(nums[k:])
        
        