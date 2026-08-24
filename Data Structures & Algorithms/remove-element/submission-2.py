class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
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
        if nums[left]==val:
            return left
        else:
            return left+1

        