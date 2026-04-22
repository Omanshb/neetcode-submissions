# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []

        curr = head
        prev = None
        counter = 0
        while curr:
            if counter % k == 0:
                if prev:
                    prev.next = None
                lst.append(curr)
            
            prev = curr
            curr = curr.next
            counter += 1
        
        
        dummy = ListNode()
        full = dummy

        for i in range(len(lst)):
            if i == len(lst) - 1:
                if counter % k != 0:
                    full.next = lst[i]
                    continue
            start = lst[i]
            curr = lst[i]
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            full.next = prev
            full = start
        
        return dummy.next






                