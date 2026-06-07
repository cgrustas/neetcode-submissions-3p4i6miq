class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        adj_list = defaultdict(set)
        visit = set()
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        def dfs(node, parent):
            if node in visit:
                return
            
            visit.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                
                dfs(neighbor, node)

            
        for i in range(n):
            if i not in visit:
                dfs(i, i - 1)
                connected += 1

        return connected