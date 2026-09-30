# The idea is to keep changing the first element in each permutation, e.g. first 1 is the first element, then 2 is the first element, then 3. And this pattern also applies to all smaller permutations. So everytime we swap element at i with element at index 
class Solution:
    res=list()
    def backtrack(self, nums, sub, index):
        if len(sub)==len(nums):
            Solution.res.append(sub.copy())
        for i in range(index,len(nums)):
            nums[index], nums[i]=nums[i], nums[index]
            sub.append(nums[index])
            self.backtrack(nums, sub, index+1)
            sub.pop()
            nums[index], nums[i]=nums[i], nums[index]
    def permute(self, nums: List[int]) -> List[List[int]]:
        Solution.res.clear()
        self.backtrack(nums, [], 0)
        return Solution.res
        