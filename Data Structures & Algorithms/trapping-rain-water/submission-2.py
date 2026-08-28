class Solution:
    def trap(self, height: List[int]) -> int:
        # this solution uses O(1) extra space.
        # this is the optimized version of the solution that used an array to store max_left and max_right heights for each element. 
        # we use 2 pointers starting at the beginning and end of the array. initially max_left and max_right are 0 for the first and last elements. We always want to calculate the trapped water between the taller heights so we compare current max_left and max_right and we increment the pointer for whichever one is less. before we increment we can calculate the area. But how? this works because we always do min(max_left, max_right). let's say if the lesser one in this case is max_left then we don't even know what max_right is. 
        max_left=0
        max_right=0
        left=0
        right=len(height)-1
        res=0
        while left<right:
            if height[left]<=height[right]:
                curr=max_left-height[left]
                if curr<0:
                    curr=0
                res+=curr
                max_left=max(max_left, height[left])
                left+=1
            else:
                curr=max_right-height[right]
                if curr<0:
                    curr=0
                res+=curr
                max_right=max(max_right, height[right])
                right-=1
        return res
        
        