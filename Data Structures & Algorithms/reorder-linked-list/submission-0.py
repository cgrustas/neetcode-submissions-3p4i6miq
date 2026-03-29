# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast/slow solution
        slow, fast = head, head.next

        # find midpoint of list with slow/fast pointer technique
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # break into two lists
        second = slow.next
        slow.next = None

        # reverse the second half of the list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halves of the list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

