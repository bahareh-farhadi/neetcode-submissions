class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # n ^ n =0
        # 0 ^ n =n 
        # so if all are appearing twice we will have 0^n where n is the number that is only appearing once
        res=0
        for num in nums:
            res=res^num
        return res

        