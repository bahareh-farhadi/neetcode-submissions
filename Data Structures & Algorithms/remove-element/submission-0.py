class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            if nums[right]==val:
                right-=1
            elif nums[left]==val:
                nums[left]=nums[right]
                nums[right]=val
                right-=1
                left+=1
            else:
                left+=1
        res=0
        for i in range(len(nums)):
            if nums[i]!=val:
                res+=1
            else:
                nums[i]=None
        return res
        