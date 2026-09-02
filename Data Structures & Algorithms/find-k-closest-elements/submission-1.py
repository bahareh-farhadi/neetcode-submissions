class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_low=None
        closest_high=None
        low=0
        high=k-1
        curr_sum=0
        min_sum=float('inf')
        for i in range(low, high+1):
            curr_sum+=abs(arr[i]-x)
        while high<len(arr):
            if curr_sum<min_sum:
                min_sum=curr_sum
                closest_low=low
                closest_high=high
                curr_sum-=abs(arr[low]-x)
                low+=1
                high+=1
                if high<len(arr):
                    curr_sum+=abs(arr[high]-x)
            else:
                # no need to update closest indices
                curr_sum-=abs(arr[low]-x)
                low+=1
                high+=1
                if high<len(arr):
                    curr_sum+=abs(arr[high]-x)

        return arr[closest_low:closest_high+1]
            
        