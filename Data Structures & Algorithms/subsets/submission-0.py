class Solution:
    res=list()
    def backtrack(self, nums, i, subset):
        Solution.res.append(subset.copy())
        for j in range(i, len(nums)):
            subset.append(nums[j])
            self.backtrack(nums, j + 1, subset)
            subset.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Solution.res.clear()
        self.backtrack(nums, 0, [])
        return Solution.res
        