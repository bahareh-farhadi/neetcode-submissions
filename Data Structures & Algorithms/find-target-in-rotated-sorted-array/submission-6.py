class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is another solution which can solve the problem by just doing one pass. we have to do nums[low]<=target<nums[mid] if that applied then we know target is in the left side, if not on the right side.
        # Note: this only works when values are uniqe, it won't work if the values are duplicate
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[mid]<=nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            
        return -1        