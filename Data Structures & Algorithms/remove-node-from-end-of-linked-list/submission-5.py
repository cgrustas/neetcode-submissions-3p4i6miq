# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        first, second = head, dummy

        # if there's only one node in the list, remove the head from the list 

        # move first pointer n steps ahead
        for _ in range(n):
            first = first.next
        
        # if first is None, then n is the first node in the list
        
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next        
        


