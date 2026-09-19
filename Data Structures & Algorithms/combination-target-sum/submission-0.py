class Solution:
    res=list()
    def backtrack(self, nums, target, i, curr_sum, subset):
        if curr_sum>target:
            return False
        if curr_sum==target:
            Solution.res.append(subset.copy())
            return
        for j in range(i, len(nums)):
            # make a choice
            subset.append(nums[j])
            curr_sum+=nums[j]

            #backtrack
            if curr_sum<target:
                # making the same choice until the current sum is less than target, once greater we advance to the next character
                self.backtrack(nums, target, j, curr_sum, subset)
            else:
                self.backtrack(nums, target, j+1, curr_sum, subset)

            #undo the choice
            subset.pop()
            curr_sum-=nums[j]
            
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        Solution.res.clear()
        self.backtrack(nums, target, 0, 0, [])
        return Solution.res
        