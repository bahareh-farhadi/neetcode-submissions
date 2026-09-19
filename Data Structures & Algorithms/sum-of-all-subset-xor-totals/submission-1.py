# The backtracking solution. 
# The recursive solution has time complexity O(2^n) but this has time complexity O(n*2^n) because we are exploring 2^n worst case for every element
# both have space complexity of O(n) because that is the maximum number of recursive calls each time worst case scenario.
class Solution:
    total=0
    def dfs(self, nums, i, subset):
        # calculate the total sum xor of the current subset passed
        curr_xor=0
        for num in subset:
            curr_xor=curr_xor^num
        Solution.total+=curr_xor

        for j in range(i, len(nums)):
            # make a choice
            subset.append(nums[j])
            #backtrack
            self.dfs(nums, j+1, subset)
            # undo the choice
            subset.pop()
        
    def subsetXORSum(self, nums: List[int]) -> int:
        Solution.total=0
        self.dfs(nums, 0, [])
        return Solution.total
        