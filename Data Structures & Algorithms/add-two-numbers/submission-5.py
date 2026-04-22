# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            op1 = l1.val if l1 else 0
            op2 = l2.val if l2 else 0
            digit = (op1 + op2 + carry) % 10
            carry = (op1 + op2 + carry) // 10
            new = ListNode(digit)
            curr.next = new
            curr = new
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            new = ListNode(carry)
            curr.next = new
            curr = new

        return dummy.next
        


        