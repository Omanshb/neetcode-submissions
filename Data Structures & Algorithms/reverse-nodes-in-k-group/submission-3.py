# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr and counter < k:
            curr = curr.next
            counter += 1
        
        if counter == k:
            curr = self.reverseKGroup(curr, k)
            while counter > 0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                counter -= 1
            head = curr
        return head

"""
Intuition: There are many tedious ways to solve this problem and then there is this approach which is very clean.
Essentially, we are using recursion to solve the problem step by step. At every given point, we first extract the 
first k elements in the linked list. You want to first do reverseKGroup on the rest of the array and then come back
to these k elements and reverse them. If you don't have k elements, just return the head itself. This is a very clever 
way of approaching this problem because reverseKGroup(full array) = reversed(first k elements) + reverseKGroup(rest of array).

Time Complexity: O(n) since we're just recursing linearly through the linked list and reversing k at a time.

Space Complexity: O(n/k) since we will have n/k recursions and that's how deep the function stack ultimately gets.
"""