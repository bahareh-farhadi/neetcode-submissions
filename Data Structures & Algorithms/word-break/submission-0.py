# top-down approach
class Solution:
    dp=dict()
    def helper(self, s):
        if len(s)==0:
            return True
        if s in Solution.dp:
            return Solution.dp[s]
        for i in range(len(s)):
            if s[:i+1] in Solution.dp and Solution.dp[s[:i+1]]==True:
                if s[i+1:] in Solution.dp:
                    if Solution.dp[s[i+1:]]==True:
                        Solution.dp[s]=True
                        return True
                else:
                    res=self.helper(s[i+1:])
                    if res==True:
                        Solution.dp[s]=True
                        return True
            
                
                
            
        Solution.dp[s]=False
        return False
        
            
                

                

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Solution.dp.clear()
        for item in wordDict:
            Solution.dp[item]=True
        self.helper(s)
        return Solution.dp[s]
        