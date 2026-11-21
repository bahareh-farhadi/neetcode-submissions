import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        min_heap = list() # (diff, row, col)
        visited = set()
        effort = 0
        heapq.heappush(min_heap, (0, 0, 0))
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while min_heap:
            elem = heapq.heappop(min_heap)
            height_diff = elem[0]
            row = elem[1]
            col = elem[2]
            if (row, col) in visited:
                continue
            visited.add((row, col))
            effort = max(effort, height_diff)
            if row == rows - 1 and col == cols - 1:
                # reached end
                return effort
            for dir in dirs:
                next_row = row + dir[0]
                next_col = col + dir[1]
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    heapq.heappush(min_heap, (abs(heights[row][col]-heights[next_row][next_col]), next_row, next_col))
            



        