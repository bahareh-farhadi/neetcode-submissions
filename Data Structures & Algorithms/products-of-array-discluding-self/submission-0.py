class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_sum=list()
        left_sum.append(1)
        for i in range(len(nums)):
            left_sum.append(left_sum[-1]*nums[i])
        right_sum=list()
        right_sum.append(1)
        for i in range(len(nums)-1, -1, -1):
            right_sum.append(right_sum[-1]*nums[i])
        # reverse right_sum
        low=0
        high=len(right_sum)-1
        while low<high:
            temp=right_sum[low]
            right_sum[low]=right_sum[high]
            right_sum[high]=temp
            low+=1
            high-=1
        left_sum=left_sum[:-1]
        right_sum=right_sum[1:]
        res=list()
        for i in range(len(nums)):
            res.append(left_sum[i]*right_sum[i])
        return res
        