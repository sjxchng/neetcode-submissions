class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot_if_fresh(r, c):
            '''
            change cell (r, c) to 2 (rotten) if it's valid
            valid means if cell is 1 (fresh) and cell is in bounds
            also append to queue q
            '''
            # if out of bounds
            if r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c:
                return 
            # if cell is empty (0)
            if grid[r][c] == 0:
                return
            # if valid
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))

        q = deque()
        # initialize with rotten fruits
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        time = 0
        # quick note:
        # while loop conditions are only checked in the beginning of each iteration
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rot_if_fresh(r + 1, c)
                rot_if_fresh(r - 1, c)
                rot_if_fresh(r, c + 1)
                rot_if_fresh(r, c - 1)
            if q:
                time += 1
            
        # if zero fresh fruits remaining
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return time
