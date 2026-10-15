class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # keep track of visited cells 
        visited = set()

        # used to mark cells as visited
        def dfs(r, c):
            # check bounds as well
            if r < 0 or rows <= r or c < 0 or cols <= c:
                return
            # if cell is water or cell is in visited set:
            if grid[r][c] == '0' or (r, c) in visited:
                return
            # if cell is land
            else:
                # mark in visited, then
                visited.add((r, c))
                # explore adjacent cells and check if they're land
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        # keep track of # of islands
        res = 0
        # go thru each cell
        for r in range(rows):
            for c in range(cols):
                # if current cell is 1 and not in visited, increase # of islands
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                # run dfs for this cell
                dfs(r, c)
        
        return res


