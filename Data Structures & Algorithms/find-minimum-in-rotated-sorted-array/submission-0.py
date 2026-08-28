class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if mid>0:
                prev=mid-1
            else:
                prev=len(nums)-1
            
            if mid<len(nums)-1:
                next=mid+1
            else:
                next=0
            
            if nums[mid]<nums[prev] and nums[mid]<nums[next]:
                return nums[mid]
            elif nums[mid]>nums[-1]:
                low=mid+1
            else:
                high=mid-1
        
        