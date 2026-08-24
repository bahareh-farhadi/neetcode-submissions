class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(1, len(strs)):
            if len(strs[i])==0:
                prefix=""
                break
            for j in range(min(len(prefix), len(strs[i]))):
                if prefix[j]!=strs[i][j]:
                    prefix=prefix[:j]
                    break
            if len(prefix)==0:
                break
            if len(prefix)>len(strs[i]):
                prefix=prefix[:len(strs[i])]
        return prefix
        