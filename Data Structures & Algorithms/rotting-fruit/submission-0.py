class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        q = collections.deque()

        # add rotten fruit to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # bfs all rotten fruit
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while q and fresh > 0: 
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or 
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            
            minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes