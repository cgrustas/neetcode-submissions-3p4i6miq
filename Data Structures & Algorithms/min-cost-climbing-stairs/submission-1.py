class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [None] * len(cost)
        
        def dfs(i):
            if i >= len(cost):
                return 0

            if not cache[i]:
                cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return cache[i]

        # You may choose to start at the index 0 or the index 1 floor.
        return min(dfs(0), dfs(1))