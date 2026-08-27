class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=list()
        i=0
        while i<len(nums):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            next_i=i+1
            while next_i<len(nums):
                if next_i>i+1 and nums[next_i]==nums[next_i-1]:
                    next_i+=1
                    continue
                low=next_i+1
                high=len(nums)-1
                need=target-(nums[i]+nums[next_i])
                while low<high:
                    if low>next_i+1 and nums[low]==nums[low-1]:
                        low+=1
                        continue
                    if high<len(nums)-1 and nums[high]==nums[high+1]:
                        high-=1
                        continue
                    curr=nums[low]+nums[high]
                    if curr==need:
                        res.append([nums[i], nums[next_i], nums[low], nums[high]])
                        low+=1
                        high-=1
                    elif curr<need:
                        low+=1
                    elif curr>need:
                        high-=1
                next_i+=1
            i+=1
        return res
        

                

        