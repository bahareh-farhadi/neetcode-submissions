class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=dict()
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        bucket=list()
        for i in range(len(nums)):
            bucket.append([])
        for key,val in freq.items():
            bucket[val-1].append(key)
        res=list()
        j=len(bucket)-1
        while k>0:
            while len(bucket[j])==0:
                j-=1
            for b in bucket[j]:
                res.append(b)
                k-=1
                if k==0:
                    break
            j-=1
        return res

                    

            
            
        