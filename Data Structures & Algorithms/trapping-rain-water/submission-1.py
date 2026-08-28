class Solution:
    def trap(self, height: List[int]) -> int:
        # this solution uses O(n) extra memory
        # the idea is that for each height we calculate the water that is trapped on top of it. The amount will be min(max_left_height, max_right_height)-height[i]. We know that the taller heights determine the water trapped, but we always get the minimum. And also we do the subtraction because we can't count the black blocks.
        max_left=list()
        max_right=list()
        max_left.append(0)
        for i in range(len(height)):
            max_right.append(0)
        for i in range(1, len(height)):
            max_left.append(max(max_left[-1], height[i-1]))
        for i in range(len(height)-2, -1, -1):
            max_right[i]=max(max_right[i+1], height[i+1])

        res=0
        for i in range(len(height)):
            curr=min(max_left[i], max_right[i])-height[i]
            # we don't have negative areas, so if anything becomes negative just assume it has no water trapped on it.
            if curr<0:
                curr=0
            res+=curr
        return res       