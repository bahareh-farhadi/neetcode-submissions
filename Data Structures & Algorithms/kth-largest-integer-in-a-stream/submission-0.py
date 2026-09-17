# Using a max heap and then doing self.max_heap[self.k] won't work because heap is a binary tree so elements won't be sorted
# what we do instead is that we use a min heap but we always keep k elements in it. so the kth largest element always is going to be the smallest element in the mean heap, so heap[0] 
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        heapq.heapify(self.nums)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
        
        
        
