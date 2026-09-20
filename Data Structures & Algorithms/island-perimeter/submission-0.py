from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # perimeter = if e.g. there is no neighbour on top then add 1 to the permiter
        # use bfs
        queue=deque()
        visited=set()

        # find the first 1 cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    queue.append((i,j))
                    visited.add((i,j))
                    break
        res=0
        while len(queue)>0:
            elem=queue.popleft()
            row=elem[0]
            col=elem[1]
            if row>0 and grid[row-1][col]==1:
                if (row-1, col) not in visited:
                    visited.add((row-1, col))
                    queue.append((row-1, col))
            else:
                res+=1
            
            if row<len(grid)-1 and grid[row+1][col]==1:
                if (row+1, col) not in visited:
                    visited.add((row+1, col))
                    queue.append((row+1, col))
            else:
                res+=1
            
            if col>0 and grid[row][col-1]==1:
                if (row, col-1) not in visited:
                    visited.add((row, col-1))
                    queue.append((row, col-1))
            else:
                res+=1
            
            if col<len(grid[0])-1 and grid[row][col+1]==1:
                if (row, col+1) not in visited:
                    visited.add((row, col+1))
                    queue.append((row, col+1))
            else:
                res+=1
        return res


            


                
        