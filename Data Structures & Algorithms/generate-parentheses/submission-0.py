class Solution:
    res=list()
    def backtrack(self, n, open_count, close_count, subset):
        if len(subset)==n*2:
            Solution.res.append("".join(subset.copy()))
            return
        
        # check if valid choice, make the choice, backtrack, undo the choice
        # add a (
        if open_count<n:
            subset.append("(")
            self.backtrack(n, open_count+1, close_count, subset)
            subset.pop()

        # add a )
        if close_count<n and close_count<open_count:
            subset.append(")")
            self.backtrack(n, open_count, close_count+1, subset)
            subset.pop()
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        Solution.res.clear()
        self.backtrack(n, 0, 0, [])
        return Solution.res
        