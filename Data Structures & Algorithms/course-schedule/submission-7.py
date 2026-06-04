class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        total = 0
        adj_list = defaultdict(set)

        def can_take_course(i):
            a, b = prerequisites[i]
            if a in adj_list[b] or a == b:
                return False

            adj_list[a].add(b)
            return True
        
        for i in range(len(prerequisites)):
            if not can_take_course(i):
                return False

        if not prerequisites:
            return True

        for prereqs in adj_list.values():
            if len(prereqs) == 0:
                return True
        return False
