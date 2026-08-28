class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                return mid
            left=nums[low:mid]
            right=nums[mid+1:high+1]
            if len(left)>0 and left[0]<=left[-1]:
                # ordered side is left
                if target>=left[0] and target<=left[-1]:
                    high=mid-1
                else:
                    low=mid+1
            elif len(left)>0 and left[0]>left[-1]:
                # ordered side is right
                if len(right)>0:
                    if target>=right[0] and target<=right[-1]:
                        low=mid+1
                    else:
                        high=mid-1
                else:
                    if mid<len(nums)-1:
                        if nums[mid+1]==target:
                            return mid+1
                        else:
                            high=mid-1
                    else:
                        high=mid-1
            elif len(left)==0:
                if mid>0:
                    if nums[mid-1]==target:
                        return mid-1
                    else:
                        low=mid+1
                else:
                    low=mid+1
        return -1
                
        