class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=list()
        i=0
        while i<len(nums):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
            else:
                target=-nums[i]
                low=i+1
                high=len(nums)-1
                while low<high:
                    if low>i+1 and nums[low]==nums[low-1]:
                        low+=1
                        continue
                    if high<len(nums)-1 and nums[high]==nums[high+1]:
                        high-=1
                        continue
                    curr=nums[low]+nums[high]
                    if curr==target:
                        res.append([nums[i], nums[low], nums[high]])
                        low+=1
                        high-=1
                    elif curr<target:
                        low+=1
                    elif curr>target:
                        high-=1
                i+=1
        return res



        