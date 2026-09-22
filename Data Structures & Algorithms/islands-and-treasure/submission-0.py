from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    #up
                    if i>0 and grid[i-1][j]==2147483647:
                        queue.append((i-1, j, 1))
                        grid[i-1][j]=1
                    #down
                    if i<len(grid)-1 and grid[i+1][j]==2147483647:
                        queue.append((i+1, j, 1))
                        grid[i+1][j]=1
                    #left
                    if j>0 and grid[i][j-1]==2147483647:
                        queue.append((i, j-1, 1))
                        grid[i][j-1]=1
                    #right
                    if j<len(grid[0])-1 and grid[i][j+1]==2147483647:
                        queue.append((i, j+1, 1))
                        grid[i][j+1]=1
        while len(queue)>0:
            elem=queue.popleft()
            row=elem[0]
            col=elem[1]
            dist=elem[2]
            #up
            if row>0 and grid[row-1][col]==2147483647:
                queue.append((row-1, col, dist+1))
                grid[row-1][col]=dist+1
            #down
            if row<len(grid)-1 and grid[row+1][col]==2147483647:
                queue.append((row+1, col, dist+1))
                grid[row+1][col]=dist+1
            #left
            if col>0 and grid[row][col-1]==2147483647:
                queue.append((row, col-1, dist+1))
                grid[row][col-1]=dist+1
            #right
            if col<len(grid[0])-1 and grid[row][col+1]==2147483647:
                queue.append((row, col+1, dist+1))
                grid[row][col+1]=dist+1
        
        