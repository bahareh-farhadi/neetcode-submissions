class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # numbers 0 to n will have a sum of n(n+1)/2
        # n will be len(nums)
        n=len(nums)
        total=n*(n+1)/2
        curr=0
        for num in nums:
            curr+=num
        return int(total-curr)
        
        