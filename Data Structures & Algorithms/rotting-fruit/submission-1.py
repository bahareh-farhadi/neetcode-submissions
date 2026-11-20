class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 2:
                    continue
                queue.append((i, j, 0))

        while queue:
            elem = queue.popleft()
            row = elem[0]
            col = elem[1]
            minute = elem[2]
            res = max(res, minute)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    queue.append((nr, nc, minute + 1))
                    grid[nr][nc] = 2
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res