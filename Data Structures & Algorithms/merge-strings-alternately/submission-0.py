class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        res=""
        turn=True
        while i<len(word1) and j<len(word2):
            if turn==True:
                res+=word1[i]
                i+=1
                turn=False
            else:
                res+=word2[j]
                j+=1
                turn=True
        while i<len(word1):
            res+=word1[i]
            i+=1
        while j<len(word2):
            res+=word2[j]
            j+=1
        return res

            

        