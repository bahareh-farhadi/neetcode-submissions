from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    queue.append((i,j))
                    num_islands+=1
                    while len(queue)>0:
                        elem=queue.popleft()
                        row=elem[0]
                        col=elem[1]
                            
                        if row>0 and grid[row-1][col]=="1":
                            grid[row-1][col]="0" #mark as visited
                            queue.append((row-1, col))

                        if row<len(grid)-1 and grid[row+1][col]=="1":
                            grid[row+1][col]="0"
                            queue.append((row+1, col))

                        if col>0 and grid[row][col-1]=="1":
                            grid[row][col-1]="0"
                            queue.append((row, col-1))
                            
                        if col<len(grid[0])-1 and grid[row][col+1]=="1":
                            grid[row][col+1]="0"
                            queue.append((row, col+1))
        return num_islands

        
        