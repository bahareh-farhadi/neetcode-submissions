class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we use binary search to solve this.
        # 1. we have to make sure nums1 has shorter length than nums2, if not we swap them
        # 2. then we calculate mid on nums1, and we know what half the total 2 arrays would be, so total-length(0 to mid) would be the length of the left sub-array on nums2. 
        # 3. check if the 2 left sub-arrays on nums1 and nums2 are valid. the last element on each sub-array has to be less than or equal to the first element on the right sub-array of the oppositu array, e.g. nums1[:mid+1][-1]<=nums2[element][0] and vice versa.
        # if leftB not less than rightA then we have to take the bigger side of A so we do low=mid+1, elif leftA not less than rightB then we have to take the smaller side of A so we high=mid-1
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        total_len=len(nums1)+len(nums2)
        len_sub=(total_len+1)//2
        low_1=0
        high_1=len(nums1)-1
        low_2=0
        high_2=len(nums2)-1
        while True:
            mid_1=(low_1+high_1)//2
            len_left=mid_1+1
            len_right=len_sub-len_left
            left_1=nums1[:mid_1+1]
            if len(left_1)>0:
                left_1=left_1[-1]
            else:
                left_1=-float('inf')
            left_2=nums2[0:len_right]
            if len(left_2)>0:
                left_2=left_2[-1]
            else:
                left_2=-float('inf')
            right_1=nums1[mid_1+1:]
            if len(right_1)>0:
                right_1=right_1[0]
            else:
                right_1=float('inf')
            right_2=nums2[len_right:]
            if len(right_2)>0:
                right_2=right_2[0]
            else:
                right_2=float('inf')

            if left_1<=right_2 and left_2<=right_1:
                if total_len%2==0:
                    return (max(left_1, left_2)+min(right_1, right_2))/2
                else:
                    return max(left_1, left_2)
            elif left_1>right_2:
                high_1=mid_1-1
            elif left_2>right_1:
                low_1=mid_1+1
        
        