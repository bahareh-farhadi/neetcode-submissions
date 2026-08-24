class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # we have to calculate the prefix sum of every element here
        # formula will be prefix_sum[r][c]=prefix_sum[r-1][c]+prefix_sum[r][c-1]-prefix_sum[r-1][c-1] (we subtract prefix_sum[r-1][c-1] because we are claculating that twice) 
        # note we have to add an extra column and an extra row of all 0's to the beginning of the prefix sum matrix to handle the edge row and ege col
        self.prefix=list()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows+1):
            temp=list()
            for j in range(cols+1):
                temp.append(0)
            self.prefix.append(temp)
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                # adding matrix[i-1][j-1] because the prefix sum matrix indexes are all one extra
                self.prefix[i][j]=self.prefix[i-1][j]+self.prefix[i][j-1]+matrix[i-1][j-1]-self.prefix[i-1][j-1]
        print(self.prefix)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # the formula would be res=prefix_sum[row2][col2]-prefix_sum[row2][col1-1]-prefix_sum[row1-1][col2]+prefix_sum[row1-1][col1-1]
        # Note: in the following we are adding one to each coordinate because prefix indexes are one extra
        res=self.prefix[row2+1][col2+1]-self.prefix[row2+1][col1]-self.prefix[row1][col2+1]+self.prefix[row1][col1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)