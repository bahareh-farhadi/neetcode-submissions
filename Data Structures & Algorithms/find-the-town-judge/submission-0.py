class Solution:
    # time complexity: O(V+E) we explore every vertex and every edge once
    # space complexity: O(V) the trust_count is the length of the vertices
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count=list()
        for i in range(n+1):
            # each person has a trust count of 0
            trust_count.append(0)
        for t in trust:
            trust_count[t[0]]-=1
            trust_count[t[1]]+=1
        for i in range(1, n+1):
            if trust_count[i]==n-1:
                # everybody trusts the judge except themselves
                return i
        return -1
        
        