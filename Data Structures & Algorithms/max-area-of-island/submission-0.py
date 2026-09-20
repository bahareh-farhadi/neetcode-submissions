from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0 #mark as visited
                    queue.append((i,j))
                    curr_area=1
                    while len(queue)>0:
                        elem=queue.popleft()
                        row=elem[0]
                        col=elem[1]

                        if row>0 and grid[row-1][col]==1:
                            grid[row-1][col]=0
                            queue.append((row-1, col))
                            curr_area+=1
                        
                        if row<len(grid)-1 and grid[row+1][col]==1:
                            grid[row+1][col]=0
                            queue.append((row+1, col))
                            curr_area+=1
                        
                        if col>0 and grid[row][col-1]==1:
                            grid[row][col-1]=0
                            queue.append((row, col-1))
                            curr_area+=1
                        
                        if col<len(grid[0])-1 and grid[row][col+1]==1:
                            grid[row][col+1]=0
                            queue.append((row, col+1))
                            curr_area+=1
                    max_area=max(max_area, curr_area)
        return max_area


        