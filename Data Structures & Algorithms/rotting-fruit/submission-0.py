from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        max_min=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j,0))
        while len(queue)>0:
            elem=queue.popleft()
            row=elem[0]
            col=elem[1]
            minute=elem[2]
            max_min=max(max_min, minute)
            #up
            if row>0 and grid[row-1][col]==1:
                queue.append((row-1, col, minute+1))
                grid[row-1][col]=2
            #down
            if row<len(grid)-1 and grid[row+1][col]==1:
                queue.append((row+1, col, minute+1))
                grid[row+1][col]=2
            #left
            if col>0 and grid[row][col-1]==1:
                queue.append((row, col-1, minute+1))
                grid[row][col-1]=2
            #right
            if col<len(grid[0])-1 and grid[row][col+1]==1:
                queue.append((row, col+1, minute+1))
                grid[row][col+1]=2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return max_min

        