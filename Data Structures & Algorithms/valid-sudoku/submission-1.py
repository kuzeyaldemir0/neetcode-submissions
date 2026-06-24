class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Let's create a list of sets
        rows = []
        columns = []
        sub_boxes = []
        count = 0
        for i in range(9):
            row = set()
            rows.append(row)
        for i in range(9):
            column = set()
            columns.append(column)
        for i in range(9):
            sub_box = set()
            sub_boxes.append(sub_box)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] not in rows[i] and board[i][j] not in columns[j] and board[i][j] not in sub_boxes[3*(i//3) + (j//3)] and board[i][j] != ".":
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    sub_boxes[3*(i//3) + (j//3)].add(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False
        return True