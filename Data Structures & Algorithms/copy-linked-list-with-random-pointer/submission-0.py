"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = dict()

        tail = head
        while tail: 
            copies[tail] = Node(tail.val)
            tail = tail.next

    
        new_head = None
        new_prev = None
        while head:
            new_tail = copies[head]
            if new_prev:
                new_prev.next = new_tail
            else: # if this is the first node
                new_head = new_tail

            if head.random:
                new_tail.random = copies[head.random]
                        
            new_prev = new_tail
            head = head.next
        
        return new_head
