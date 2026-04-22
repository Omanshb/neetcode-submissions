# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        ln = 0
        while curr != None:
            ln += 1
            curr = curr.next

        dummy = curr = ListNode(0, head)
        for i in range(ln - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next