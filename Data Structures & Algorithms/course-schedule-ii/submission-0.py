class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set)
        res = []
        visit = set()
        cycle = set()


        for courseNum in range(numCourses):
            adj_list[courseNum] = set()
            
        for a, b in prerequisites:
            adj_list[a].add(b)
        
        def dfs(a): 
            if a in cycle:
                return False
            
            if a in visit:
                return True
            
            cycle.add(a)
            for b in adj_list[a]:
                if not dfs(b):
                    return False
            
            res.append(a)
            visit.add(a)
            cycle.remove(a)
            return True
            
        for a in range(numCourses):
            if not dfs(a):
                return []
        
        return res
                       

