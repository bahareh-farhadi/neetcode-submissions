class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while i<=j and j<len(nums):
            if nums[i]!=0:
                i+=1
                j+=1
            else:
                if nums[j]!=0:
                    nums[i]=nums[j]
                    nums[j]=0
                    i+=1
                    j+=1
                else:
                    j+=1
        
        
        