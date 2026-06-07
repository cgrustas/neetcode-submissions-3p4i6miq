class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        adj_list = defaultdict(list)
        visit = set()
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for neighbor in adj_list[node]:                
                dfs(neighbor)

            
        for i in range(n):
            if i not in visit:
                dfs(i)
                connected += 1

        return connected