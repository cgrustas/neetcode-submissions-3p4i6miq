class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        def path_already_exists(source, target, visit):
            if source == target:
                return True
            
            visit.add(source)
            for neighbor in adj_list[source]:
                if neighbor not in visit:
                    if path_already_exists(neighbor, target, visit):
                        return True
            return False
        
        for a, b in edges:
            visit = set()
            if a in adj_list and b in adj_list and path_already_exists(a, b, visit):
                return [a, b]
            
            adj_list[a].append(b)
            adj_list[b].append(a)
        
