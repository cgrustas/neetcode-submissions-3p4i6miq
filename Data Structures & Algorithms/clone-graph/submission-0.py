"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(current_node):
            if current_node in old_to_new:
                return old_to_new[current_node]

            clone = Node(current_node.val)
            old_to_new[current_node] = clone
            for neighbor in current_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                clone.neighbors.append(cloned_neighbor)
            
            return clone
                


        return dfs(node)

