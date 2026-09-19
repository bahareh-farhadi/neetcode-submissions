# The recusrive solution: The idea is that we will have 2^n possibilities, because each element can be in the sum XOR or not every time.
class Solution:
    def dfs(self, nums, i, total):
        if i==len(nums):
            # have looked at all elements
            return total
        including_current_element = self.dfs(nums, i+1, total^nums[i])
        excluding_current_element = self.dfs(nums, i+1, total)
        return including_current_element+excluding_current_element
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, 0)
        