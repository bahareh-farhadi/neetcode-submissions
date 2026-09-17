import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap of length k, if the length exceeds k pop the first element. at the end return the first element in the heap as that is going to be the largest k element
        min_heap=list()
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]
        