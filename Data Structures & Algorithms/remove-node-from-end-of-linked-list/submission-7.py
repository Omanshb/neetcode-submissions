# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        counter = 0
        while counter < length - n:
            curr = curr.next
            counter += 1
        
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return dummy.next