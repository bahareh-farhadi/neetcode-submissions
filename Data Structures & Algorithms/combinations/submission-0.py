class Solution:
    res=list()
    def backtrack(self, n, k, i, subset):
        if len(subset)==k:
            Solution.res.append(subset.copy())
            return #we return because we don't want to explore more options
        for j in range(i, n+1):
            # make a choice
            subset.append(j)
            # backtrack
            self.backtrack(n, k, j+1, subset)
            # undo the choice
            subset.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        Solution.res.clear()
        self.backtrack(n, k, 1, [])
        return Solution.res
        