
# the non-optimal solution - doing a dfs/bfs starting from each node 
# the optimal solution uses 2d dp
# the idea is that we initialize dp to 0 for every element. If an element is non-zero we know we have already explored it and we know the longest path from that element. 
# if not then we start a dfs from that element, we add all elements larger than the current element whose value has not been calculated yet into the stack. If the value is calculated then we update the current's value.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp=list()
        for i in range(len(matrix)):
            temp=list()
            for j in range(len(matrix[0])):
                temp.append(0)
            dp.append(temp)

        max_len=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j]!=0:
                    continue
                stack=list()
                # False means its neighbours have not been explored yet
                stack.append((i,j,False))
                while len(stack)>0:
                    elem=stack.pop()
                    row=elem[0]
                    col=elem[1]
                    status=elem[2]
                    
                    if dp[row][col]!=0:
                        continue
                    if status==True:
                        # all neibours have been explored
                        dp[row][col]=1
                        #up
                        if row>0 and matrix[row-1][col]>matrix[row][col]:
                            dp[row][col]=max(dp[row][col], 1+dp[row-1][col])
                        #down
                        if row<len(dp)-1 and matrix[row+1][col]>matrix[row][col]:
                            dp[row][col]=max(dp[row][col], 1+dp[row+1][col])
                        #left
                        if col>0 and matrix[row][col-1]>matrix[row][col]:
                            dp[row][col]=max(dp[row][col], 1+dp[row][col-1])
                        #right
                        if col<len(dp[0])-1 and matrix[row][col+1]>matrix[row][col]:
                            dp[row][col]=max(dp[row][col], 1+dp[row][col+1])
                        max_len=max(max_len, dp[row][col])
                    else:
                        # add it back to the stack so we explore it after we are done with the neighbours
                        stack.append((row, col, True))
                        #up
                        if row>0 and matrix[row-1][col]>matrix[row][col] and dp[row-1][col]==0:
                            stack.append((row-1, col, False))
                        #down
                        if row<len(dp)-1 and matrix[row+1][col]>matrix[row][col] and dp[row+1][col]==0:
                            stack.append((row+1, col, False))
                        #left
                        if col>0 and matrix[row][col-1]>matrix[row][col] and dp[row][col-1]==0:
                            stack.append((row, col-1, False))
                        #right
                        if col<len(dp[0])-1 and matrix[row][col+1]>matrix[row][col] and dp[row][col+1]==0:
                            stack.append((row, col+1, False))
        

        return max_len


        