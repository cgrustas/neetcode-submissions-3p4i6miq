class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        visit = set()

        if len(edges) != n - 1:
            return False

        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        def dfs(node):
            if node in visit:
                return True

            visit.add(node)
            for child in adj_list[node]:
                if not dfs(child):
                    return False
            return True
        
        dfs(0)
        return True if len(visit) == n else False