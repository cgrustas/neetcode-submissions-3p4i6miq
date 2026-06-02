class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        res = []
        
        def dfs(r, c, visited_set, prev_height):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or 
                (r, c) in visited_set or
                heights[r][c] < prev_height):
                return
            
            visited_set.add((r, c))
            dfs(r + 1, c, visited_set, heights[r][c])
            dfs(r - 1, c, visited_set, heights[r][c])
            dfs(r, c + 1, visited_set, heights[r][c])
            dfs(r, c - 1, visited_set, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific_visited, heights[r][0])
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pacific_visited, heights[0][c])
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS - 1][c])
    
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic_visited and (r, c) in pacific_visited:
                    res.append([r, c])

        return res