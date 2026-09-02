class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we will use a combination of binary search and greedy algorithm for this. the idea is to use low=maximum element in the array and high=sum of all the elements and do a binary search on this. 
        # mid=(low+high)/2 for each mid we start adding elements from the beginning of the array until the sum is greater than mid. once the sum becomes greater than mid we restart the sum and start adding from that element on. every time we restart the sum we count a new sub-array. at the end we calculate whether the num of sub-arrays is less than or equal to k, if so then we do high=mid-1 (meaning we can do better than that), else we do low=mid+1 (meaning we need to decrease the number of sub-arrays so our sum will be bigger)
        low=-float('inf')
        high=0
        for num in nums:
            low=max(low, num)
            high+=num
        res=high
        while low<=high:
            mid=int((low+high)/2)
            curr_sum=0
            num_sub_arrays=0
            for num in nums:
                curr_sum+=num
                if curr_sum>mid:
                    curr_sum=num
                    num_sub_arrays+=1
            num_sub_arrays+=1
            if num_sub_arrays<=k:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res

        
            
        