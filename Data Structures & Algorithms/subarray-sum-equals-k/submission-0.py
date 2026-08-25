class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen=dict()
        seen[0]=1 #before the array begins
        prefix_sum=list()
        prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        print(prefix_sum)
        res=0
        for p in prefix_sum:
            if p-k in seen:
                res+=seen[p-k]
            if p in seen:
                seen[p]+=1
            else:
                seen[p]=1
        return res


        