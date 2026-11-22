from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        visited = dict() # key: coordinates, val: number of obstacles eliminated
        queue = deque() # (row, col, steps, obstacles eliminated)
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            queue.append((0, 0, 0, 1))
            visited[(0, 0)] = 1
        else:
            queue.append((0, 0, 0, 0))
            visited[(0, 0)] = 0
        
        dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        while queue:
            elem = queue.popleft()
            row = elem[0]
            col = elem[1]
            steps = elem[2]
            obs = elem[3]
            if row == rows - 1 and col == cols - 1:
                return steps
            for dir in dirs:
                nr, nc = row + dir[0], col + dir[1]
                if 0 <= nr < rows and 0<= nc < cols:
                    if grid[nr][nc] == 1:
                        if obs + 1 <= k:
                            if (nr, nc) in visited:
                                if 1 + obs < visited[(nr, nc)]:
                                    visited[(nr, nc)] = 1 + obs
                                    queue.append((nr, nc, steps + 1, obs + 1))
                            else:
                                visited[(nr, nc)] = 1 + obs
                                queue.append((nr, nc, steps + 1, obs + 1))
                    else:
                        if (nr, nc) in visited:
                            if obs < visited[(nr, nc)]:
                                visited[(nr, nc)] = obs
                                queue.append((nr, nc, steps + 1, obs))
                        else:
                            visited[(nr, nc)] = obs
                            queue.append((nr, nc, steps + 1, obs))
        return -1
                            


            
        
        
