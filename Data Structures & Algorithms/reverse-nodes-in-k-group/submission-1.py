# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # perhaps pass through once to determine the size of the list (n)?
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1

        if n < k:
            return head

        # reverse this list, and connect the reversed tail to the rest of the list
        prev = None
        curr = head
        for _ in range(k): 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # get rest of list
        new_head, new_tail = prev, head
        
        rest_of_original_list = curr
        new_tail.next = self.reverseKGroup(rest_of_original_list, k)

        return new_head
    