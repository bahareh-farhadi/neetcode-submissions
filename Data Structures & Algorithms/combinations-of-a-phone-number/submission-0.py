class Solution:
    res=list()
    # i parses the lists in digits
    # j parses elements inside each list
    def backtrack(self, digits, i, subset):
        if len(subset)==len(digits):
            if len(subset)!=0:
                Solution.res.append("".join(subset.copy()))
        for i_ in range(i, len(digits)):
            for j_ in range(0, len(digits[i_])):
                # make a choice
                subset.append(digits[i_][j_])
                # backtrack
                self.backtrack(digits, i_+1, subset)
                # undo the choice
                subset.pop()
        


    def letterCombinations(self, digits: str) -> List[str]:
        dig_map={"2":["a", "b", "c"],
        "3":["d", "e", "f"],
        "4":["g", "h", "i"],
        "5":["j", "k", "l"],
        "6":["m", "n", "o"],
        "7":["p", "q", "r", "s"],
        "8":["t", "u", "v"],
        "9":["w", "x", "y", "z"]}
        Solution.res.clear()
        dig_modified=list()
        for d in digits:
           dig_modified.append(dig_map[d])
        self.backtrack(dig_modified, 0, [])
        return Solution.res
        