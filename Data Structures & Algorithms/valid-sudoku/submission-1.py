class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} # key = row, value = set()
        cols = {} # key = col, value = set()
        squares = {} # key = (row // 3, col // 3), value = set()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows.get(r, []) or 
                    board[r][c] in cols.get(c, []) or
                    board[r][c] in squares.get((r // 3, c // 3), [])):
                    return False
                
                if c not in cols:
                    cols[c] = set()
                if r not in rows:
                    rows[r] = set()
                if (r // 3, c // 3) not in squares:
                    squares[(r // 3, c // 3)] = set()
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
                