# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        heap = []

        counter = 0

        for l in lists:
            counter += 1
            heapq.heappush(heap, (l.val, counter, l))
        
        while heap:
            counter += 1
            topVal, c, topNode = heapq.heappop(heap)
            
            if topNode.next:
                heapq.heappush(heap, (topNode.next.val, counter, topNode.next))
            
            curr.next = topNode
            curr = curr.next

        return dummy.next
        
        