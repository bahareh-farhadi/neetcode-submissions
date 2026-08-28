class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        potential=None
        while low<=high:
            mid=int((low+high)/2)
            curr=mid*mid
            if curr==x:
                return mid
            elif curr<x:
                low=mid+1
                potential=mid
            elif curr>x:
                high=mid-1
                potential=mid-1
        return potential
        
        