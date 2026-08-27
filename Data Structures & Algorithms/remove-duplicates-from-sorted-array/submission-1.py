class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we keep a slow and fast pointer
        # the slow pointer will be kept at a duplicate and the fast pointer will iterate through the array
        # once we find 2 consecutive values we want to right them so we write nums[fast] to nums[slow] and then increment slow (and obviously fast does get incremented every iteration)

        # we start from 1 because the element at index 0 will be kept regardless
        slow=1
        fast=1
        while fast<len(nums):
            if nums[fast]!=nums[fast-1]:
                # different values
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

        