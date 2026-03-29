# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for linkedList in lists:
            # find smallest element in any of the three lists
            node = linkedList
            while node:
                # traverse through the linked list, and add all values to the heap
                heapq.heappush(heap, node.val)
                node = node.next
        
        dummy = ListNode()
        node = dummy
        for _ in range(len(heap)):
            node.next = ListNode(heapq.heappop(heap), None)
            node = node.next
        
        return dummy.next
            