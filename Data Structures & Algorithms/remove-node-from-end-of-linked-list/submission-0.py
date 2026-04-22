# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lgth = 0
        curr = head
        while curr:
            lgth += 1
            curr = curr.next

        dummy = curr = ListNode()
        curr.next = head
        for i in range(lgth - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next