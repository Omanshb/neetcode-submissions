# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        prod = 1
        curr = l1
        while curr:
            num1 += curr.val * prod
            curr = curr.next
            prod *= 10
        
        prod = 1
        curr = l2
        while curr:
            num2 += curr.val * prod
            curr = curr.next
            prod *= 10

        sm = num1 + num2
        dummy = curr = ListNode(0)
        while sm != 0:
            curr.next = ListNode(sm % 10)
            curr = curr.next
            sm = sm // 10
        return dummy.next or dummy
        