class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the idea is to first find the minimum element to see where the array is rotated from, then perform a binary search on the left sub-array and then on the right sub-array
        low=0
        high=len(nums)-1
        min_index=-1
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
            
            if nums[mid]<nums[next] and nums[mid]<nums[prev]:
                min_index=mid
                break
            else:
                if nums[mid]<nums[-1]:
                    high=mid-1
                else:
                    low=mid+1
        
        # left sub-array
        low=0
        if min_index>0:
            high=min_index-1
        else:
            high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        
        # right sub-array
        low=min_index
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        
        return -1
        
                
        