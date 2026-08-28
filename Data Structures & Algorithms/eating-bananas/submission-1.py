import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we have to determine the range of applicable numbers for k
        # minimum applicable k can be total num of bananas/hour. so this is the longest it will take to eat the bananas. 
        # maximum applicable k can be the maximum number of bananas in a pile. because if those bananas can be eaten in one hour then all other piles can each be eaten in 1 hour.
        # so we will use binary search to check which number in this range for k makes sense so the bananas are eaten in less than h hours.
        total=0
        max_val=0
        for pile in piles:
            total+=pile
            max_val=max(max_val, pile)
        
        low=math.ceil(total/h)
        high=max_val
        potential=None
        while low<=high:
            mid=int((low+high)/2)
            curr=0
            for pile in piles:
                curr+=math.ceil(pile/mid)
            if curr==h:
                # here we don't return because we might always be able to do it in less than h hours
                high=mid-1
                potential=mid
            elif curr>h:
                low=mid+1
                # we don't assign any potential here because this doesn't even meet the criteria mentioned in the question *curr always has to be less than h
            elif curr<h:
                high=mid-1
                potential=mid
        return potential
        



        