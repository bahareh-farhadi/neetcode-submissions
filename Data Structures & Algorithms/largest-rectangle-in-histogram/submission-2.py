class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the idea is that we keep adding heights and their indices to the stack .e.g. [(7:0)]
        # when we see a new element with greater height than the previoud one we add that as a new element to the stack because the previous height is shorter so it can extend and we can use its area later. But if the current height is less than the previous one because the previous one cannot extend further we have to pop it.
        # we calculate the max area when we pop elements. when we pop our height is the height we are popping and the width is from the index of the popped element to the current index. 
        # after we pop we update the index of the current element to that of the popped element since the current height can extend backwards. 
        # we need to update the max area once we are done iterating through heights, because we will have elements in stack still.
        stack=list()
        stack.append([heights[0], 0])
        max_area=0
        i=1
        while i<len(heights):
            current_index=i
            while len(stack)>0 and heights[i]<stack[-1][0]:
                last_elem=stack.pop()
                current_index=last_elem[1]
                max_area=max(max_area, last_elem[0]*(i-last_elem[1]))
            stack.append([heights[i], current_index])
            i+=1
        while len(stack)>0:
            elem=stack.pop()
            max_area=max(max_area, elem[0]*(len(heights)-elem[1]))
        return max_area
            
                
        