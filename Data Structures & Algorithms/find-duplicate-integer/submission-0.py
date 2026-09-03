class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # just remember this cuz this is popular in interviews
        # we use Floyd's algorithm for
        # 1. we set a slow pointer and a fast pointer, once they interset we have found the start of the cycle
        # 2. then we set a slow pointer at the intersection that we found already and another slow pointer at the beginning of the array. once these 2 small pointers intersect we have found our duplicate. 
        # Note: for this we have to see what each element is pointing to and advance the pointers to those. e.g. 1,2,3,2,2 the first element is 1 so it points to element at index 1, the last element is 2 so it points to the element at index 2. once the pointers intersect the index of the intersection is the number that is repeated.
        slow=0
        fast=0
        slow=nums[slow]
        fast=nums[fast]
        fast=nums[fast]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
        
        slow1=slow
        slow2=0
        while slow1!=slow2:
            slow1=nums[slow1]
            slow2=nums[slow2]
        return slow1


            
        