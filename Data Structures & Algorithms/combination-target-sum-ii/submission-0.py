class Solution:
    res=list()
    def backtrack(self, candidates, target, i, curr_sum, subset):
        if curr_sum>target:
            return
        if curr_sum==target:
            Solution.res.append(subset.copy())
        seen=set()
        for j in range(i, len(candidates)):
            if candidates[j] in seen:
                continue
            seen.add(candidates[j])
            # make a choice
            subset.append(candidates[j])
            curr_sum+=candidates[j]
            # backtrack
            self.backtrack(candidates, target, j+1, curr_sum, subset)
            # undo the choice
            curr_sum-=candidates[j]
            subset.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        Solution.res.clear()
        self.backtrack(candidates, target, 0, 0, [])
        return Solution.res
        