class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while low<high:
            curr=numbers[low]+numbers[high]
            if curr==target:
                return [low+1, high+1]
            elif curr>target:
                high-=1
            elif curr<target:
                low+=1
        
        