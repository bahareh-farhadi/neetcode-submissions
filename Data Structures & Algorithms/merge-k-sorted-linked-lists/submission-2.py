# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = list()
        min_heap = list() # (node_val, list number) 
        for i in range(len(lists)):
            if lists[i] is not None:
                node = lists[i]
                node_val = node.val
                heapq.heappush(min_heap, (node_val, i))
        root = None
        curr = None
        while min_heap:
            item = heapq.heappop(min_heap)
            list_index = item[1]
            node = lists[list_index]
            if root is None:
                root = node
                curr = root
            else:
                curr.next = node
                curr = curr.next
            res.append(node)
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, list_index))
                lists[list_index] = lists[list_index].next
        return root


        