class Solution:
    def rob(self, nums: List[int]) -> int:
        # because the houses are in a circle we solve the problem twice.
        # first we solve for the case where we rob the first house and we skip the last house, and then we solve the case where we skip the first house and rob the last house. then we return the maximum of the 2. 
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        dp_first=list()
        for i in range(len(nums)-1):
            dp_first.append(0)
        dp_first[0]=nums[0]
        dp_first[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp_first[i]=max(nums[i]+dp_first[i-2], dp_first[i-1])
        max_first=max(dp_first[-1], dp_first[-2])

        dp_last=list()
        for i in range(len(nums)):
            dp_last.append(0)
        dp_last[0]=0
        dp_last[1]=nums[1]
        dp_last[2]=max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp_last[i]=max(nums[i]+dp_last[i-2], dp_last[i-1])
        max_last=max(dp_last[-1], dp_last[-2])
        return max(max_first, max_last)
        
        
        
        
        