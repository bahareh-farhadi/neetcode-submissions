class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        low=0
        
        for i in range(low, low+k+1):
            if i<len(nums):
                if nums[i] in seen:
                    return True
                else:
                    seen.add(nums[i])
        high=low+k+1
        if k<len(nums):
            while high<len(nums):
                seen.remove(nums[low])
                if nums[high] in seen:
                    return True
                else:
                    seen.add(nums[high])
                    high+=1
                    low+=1
        return False


                
            
        
            
        