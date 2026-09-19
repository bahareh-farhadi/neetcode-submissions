class Solution:
    res=list()
    def backtrack(self, nums, i, subset):
        Solution.res.append(subset.copy())
        seen=set()
        for j in range(i, len(nums)):
            if nums[j] in seen:
                continue
            seen.add(nums[j])
            subset.append(nums[j])
            self.backtrack(nums, j + 1, subset)
            subset.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        Solution.res.clear()
        nums.sort()
        self.backtrack(nums, 0, [])
        return Solution.res
        