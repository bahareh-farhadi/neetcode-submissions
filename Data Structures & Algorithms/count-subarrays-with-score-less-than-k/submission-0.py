class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        low = 0
        high = 0
        curr_sum = 0
        res = 0
        while high < len(nums):
            curr_sum+=nums[high]
            curr_res = curr_sum * (high - low + 1)
            if curr_res < k:
                # all subarrays inside the window count (so res+=1 is wrong)
                res+=high - low + 1
                high+=1
            else:
                while low <= high:
                    curr_sum-=nums[low]
                    low+=1
                    if low <= high:
                        curr_res = curr_sum * (high - low + 1)
                        if curr_res < k:
                            res+=high - low + 1
                            break
                high+=1
        return res
