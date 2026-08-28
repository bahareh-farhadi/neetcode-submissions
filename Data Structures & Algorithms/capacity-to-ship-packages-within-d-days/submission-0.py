class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total=0
        max_weight=0
        for w in weights:
            total+=w
            max_weight=max(max_weight, w)
        
        # low is the maximum weight available, meaning in one day the heaviest package can be shipped. we don't do total/days because that could mean we have to divide one package into multiple shipments which is not correct.
        low=max_weight
        high=total
        potential=None
        while low<=high:
            mid=int((low+high)/2)
            num_days=1
            i=0
            curr=weights[i]
            while i<len(weights):
                if i+1<len(weights) and curr+weights[i+1]<=mid:
                    i+=1
                    curr+=weights[i]
                elif i+1<len(weights) and curr+weights[i+1]>mid:
                    num_days+=1
                    i+=1
                    curr=weights[i]
                else:
                    i+=1
            print(f"num_days {num_days}")
            if num_days>days:
                # not qualified, increase capacity
                low=mid+1
            else:
                # can be shipped in days or less
                high=mid-1
                potential=mid
        return potential

                
                
                
        