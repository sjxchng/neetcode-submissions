class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            row = [x for x in row if x != "."]
            if len(set(row)) != len(row):
                return False

        # check column
        cols = []
        for col in range(9):
            c = []
            for row in range(9):
                if board[row][col] != ".":
                    c.append(board[row][col])
            cols.append(c)
        for col in cols:
            if len(set(col)) != len(col):
                return False

        # check 3x3 boxes
        boxes = []
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                tmp_list = []
                for i in range(row, row + 3):
                    tmp_list += board[i][col : col + 3]
                boxes.append(tmp_list)
        for box in boxes:
            box = [item for item in box if item != "."]
            if len(set(box)) != len(box):
                return False

        # lastly,
        return True