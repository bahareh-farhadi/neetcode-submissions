class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=0
        high=len(heights)-1
        max_area=0
        while low<high:
            area=(high-low)*min(heights[low], heights[high])
            max_area=max(max_area, area)
            if heights[low]<=heights[high]:
                low+=1
            else:
                high-=1
        return max_area
        