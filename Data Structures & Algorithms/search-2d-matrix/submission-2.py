class Solution:
    def calculate_index(self, num, cols):
        row_num=num//cols
        col_num=num%cols
        return row_num, col_num
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        low=0
        high=rows*cols-1
        while low<=high:
            mid=int((low+high)/2)
            row_num, col_num = self.calculate_index(mid, cols)
            if matrix[row_num][col_num]==target:
                return True
            elif matrix[row_num][col_num]<target:
                low=mid+1
            elif matrix[row_num][col_num]>target:
                high=mid-1
        return False
        