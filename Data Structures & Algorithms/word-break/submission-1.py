class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=list()
        for i in range(len(s)):
            dp.append(False)
        dp.append(True) # the element after the last element is set to True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if dp[i]==True:
                    break
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)]
        return dp[0]


        