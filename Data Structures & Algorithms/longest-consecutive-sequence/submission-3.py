class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        seen=set()
        for num in nums:
            seen.add(num)
        res=0
        for num in seen:
            # only start counting if num is the smallest number in a sequence
            if num-1 not in seen:
                curr=num
                length=1
                while curr+1 in seen:
                    curr+=1
                    length+=1
                res=max(res, length)
        return res

            
        
        