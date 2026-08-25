class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=dict()
        cols=dict()
        squares=dict()
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                # rows
                if i in rows:
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].append(board[i][j])
                else:
                    rows[i]=[board[i][j]]
                # cols
                if j in cols:
                    if board[i][j] in cols[j]:
                        return False
                    else:
                        cols[j].append(board[i][j])
                else:
                    cols[j]=[board[i][j]]
                # squares
                squares_key=-1
                if i<3 and j<3:
                    squares_key=0
                elif i<3 and j>=3 and j<6:
                    squares_key=1
                elif i<3 and j>=6:
                    squares_key=2
                elif i>=3 and i<6 and j<3:
                    squares_key=3
                elif i>=3 and i<6 and j>=3 and j<6:
                    squares_key=4
                elif i>=3 and i<6 and j>=6:
                    squares_key=5
                elif i>=6 and j<3:
                    squares_key=6
                elif i>=6 and j>=3 and j<6:
                    squares_key=7
                elif i>=6 and j>=6:
                    squares_key=8
                if squares_key in squares:
                    if board[i][j] in squares[squares_key]:
                        return False
                    else:
                        squares[squares_key].append(board[i][j])
                else:
                    squares[squares_key]=[board[i][j]]
        return True


                

        