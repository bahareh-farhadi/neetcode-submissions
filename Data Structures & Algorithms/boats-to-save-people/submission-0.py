class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low=0
        high=len(people)-1
        res=0
        while low<=high:
            curr=people[low]+people[high]
            if curr<=limit:
                res+=1
                low+=1
                high-=1
            else:
                res+=1
                high-=1
        return res

        