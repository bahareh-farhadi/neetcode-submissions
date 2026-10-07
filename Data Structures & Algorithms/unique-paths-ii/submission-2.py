class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j]==1:
                    #obstacle
                    obstacleGrid[i][j]=-1
                else:
                    if i==0 and j==0:
                        obstacleGrid[i][j]=1
                    else:
                        if i>0:
                            if obstacleGrid[i-1][j]!=-1:
                                obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                        if j>0:
                            if obstacleGrid[i][j-1]!=-1:
                                obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        if obstacleGrid[-1][-1]==-1:
            return 0
        else:
            return obstacleGrid[-1][-1]

        
        