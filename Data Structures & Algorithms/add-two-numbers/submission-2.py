# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        curr = None

        while l1 and l2:
            total = l1.val + l2.val + carry
            
            if total < 10:
                carry = 0
            else:
                carry = 1
                total -= 10
            
            if not head:
                head = ListNode(total, None)
                curr = head
            else:
                curr.next = ListNode(total, None)
                curr = curr.next
            
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry

            if total < 10:
                l1.val += carry
                curr.next = l1
                return head

            carry = 1
            curr.next = ListNode(0, None)
            curr = curr.next
            l1 = l1.next

        while l2: 
            total = l2.val + carry

            if total < 10:
                l2.val += carry
                curr.next = l2
                return head

            carry = 1
            curr.next = ListNode(0, None)
            curr = curr.next
            l2 = l2.next

        if carry == 1:
            curr.next = ListNode(1, None)

        return head
                
