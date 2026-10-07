class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=list()
        for i in range(len(text1)):
            temp=list()
            for j in range(len(text2)):
                temp.append(0)
            dp.append(temp)
        if text1[0]==text2[0]:
            dp[0][0]=1
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i==0 and j==0:
                    continue
                if i==0:
                    if text1[i]==text2[j]:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i][j-1]

                elif j==0:
                    if text1[i]==text2[j]:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j]
                else:
                    if text1[i]==text2[j]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]
                
                
        