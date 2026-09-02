class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # unlike the other version of this question where all the elements are unique we need to be aware of the scenario where e.g. nums[low]==nums[mid] since this brings inambigiuty since we won't know what side of the array we are on. so in that scenario instead of modifying low=mi+1 or high=mid-1 we increase low by 1. (we can do the same by doing high-1 if we are comparing to the end of the array) if we have a lot of dupliocate then this could become O(n), but in the best case we can solve it in O(logn)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]==target:
                return True
            if nums[low]<nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[mid]<nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            elif nums[mid]==nums[low]:
                low+=1
            elif nums[mid]==nums[high]:
                high-=1
        return False
        