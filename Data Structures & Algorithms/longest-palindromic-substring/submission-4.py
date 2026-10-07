# two pointers approach
# time complexity O(n^2)
# space complexity O(n) for output
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=0
        res_start=None
        res_end=None
        for i in range(len(s)):
            # odd length
            low=i
            high=i
            while low>=0 and high<len(s):
                if s[low]==s[high]:
                    if high-low+1>max_len:
                        max_len=high-low+1
                        res_start=low
                        res_end=high+1
                    low-=1
                    high+=1
                else:
                    break
            # even length
            low=i
            high=i+1
            while low>=0 and high<len(s):
                if s[low]==s[high]:
                    if high-low+1>max_len:
                        max_len=high-low+1
                        res_start=low
                        res_end=high+1
                    low-=1
                    high+=1
                else:
                    break
        return s[res_start:res_end]

        