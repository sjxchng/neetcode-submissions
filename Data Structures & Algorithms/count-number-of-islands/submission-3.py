class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def mark(r, c):
            if r < 0 or c < 0 or ROWS <= r or COLS <= c:
                return 0
            if grid[r][c] == "0":
                return 0
                
            grid[r][c] = "0"

            mark(r + 1, c)
            mark(r - 1, c)
            mark(r, c + 1)
            mark(r, c - 1)
            return 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += mark(r, c)
        return res

