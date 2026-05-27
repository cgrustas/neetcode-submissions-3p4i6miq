class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(i, j):
            if (i < 0 or i >= len(grid)
                or j < 0 or j >= len(grid[0])):
                return

            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1":
                    res += 1
                    dfs(i, j) # "sink" the island
        return res

