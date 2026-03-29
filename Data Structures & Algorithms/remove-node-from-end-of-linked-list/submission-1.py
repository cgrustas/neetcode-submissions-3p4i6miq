# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        
        removeNodeIdx = length - n

        if removeNodeIdx == 0:
            head = head.next
            return head
        
        prev, curr = None, head
        for i in range(0, removeNodeIdx):
            prev = curr
            curr = curr.next
        prev.next = curr.next

        return head


