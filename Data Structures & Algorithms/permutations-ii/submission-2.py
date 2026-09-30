class Solution:
    res=list()
    def backtrack(self, nums, sub, index):
        if len(sub)==len(nums):
            Solution.res.append(sub.copy())
        seen=set()
        for i in range(index, len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[i], nums[index] = nums[index], nums[i]
                sub.append(nums[index])
                self.backtrack(nums, sub, index+1)
                sub.pop()
                nums[i], nums[index] = nums[index], nums[i]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Solution.res.clear()
        self.backtrack(nums, [], 0)
        return Solution.res
        