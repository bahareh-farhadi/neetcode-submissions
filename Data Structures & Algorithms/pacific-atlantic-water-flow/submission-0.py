class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find all nodes reachable to pacific and atlantic and then return their common elements
        # first add all nodes adjacent to the ocean, then find adjacent nodes to them that have heights higher or equal (going in reverse)
        stack = list()
        pacific = set()
        rows = len(heights)
        cols = len(heights[0])
        
        # add all cells at row 0
        for j in range(cols):
            stack.append((0, j))
            pacific.add((0, j))
        # add all cells at col 0
        for i in range(rows):
            if (i, 0) not in pacific:
                stack.append((i, 0))
                pacific.add((i, 0))

        dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        while stack:
            elem = stack.pop()
            row = elem[0]
            col = elem[1]
            for dir in dirs:
                next_row = row + dir[0]
                next_col = col + dir[1]
                if 0 <= next_row < rows and 0<= next_col < cols and heights[next_row][next_col] >= heights[row][col] and (next_row, next_col) not in pacific:
                    stack.append((next_row, next_col))
                    pacific.add((next_row, next_col))
        
        stack = list()
        atlantic = set()
        # add all cells at the last row
        for j in range(cols):
            stack.append((rows - 1, j))
            atlantic.add((rows - 1, j))

        # add all cells at the last col
        for i in range(rows):
            if (i, cols - 1) not in atlantic:
                stack.append((i, cols - 1))
                atlantic.add((i, cols - 1))

        while stack:
            elem = stack.pop()
            row = elem[0]
            col = elem[1]
            for dir in dirs:
                next_row = row + dir[0]
                next_col = col + dir[1]
                if 0 <= next_row < rows and 0<= next_col < cols and heights[next_row][next_col] >= heights[row][col] and (next_row, next_col) not in atlantic:
                    stack.append((next_row, next_col))
                    atlantic.add((next_row, next_col))
        
        res = list()
        
        for item in pacific:
            if item in atlantic:
                res.append(item)
        
        return res

            



        