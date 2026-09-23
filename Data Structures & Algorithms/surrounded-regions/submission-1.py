# any region reachable from the board O's cannot be changes to X, so we have to run a dfs or bfs on all the board O's and mark them. at the end we go over the board and any O that is not marked will be changes to X and any O that is marked will be changed back to O.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack=list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1) and board[i][j]=="O":
                    stack.append((i,j))
                    board[i][j]="T"
                    while len(stack)>0:
                        elem=stack.pop()
                        row=elem[0]
                        col=elem[1]
                        #up
                        if row>0 and board[row-1][col]=="O":

                            stack.append((row-1,col))
                            board[row-1][col]="T"
                        #down
                        if row<len(board)-1 and board[row+1][col]=="O":

                            stack.append((row+1,col))
                            board[row+1][col]="T"
                        #left
                        if col>0 and board[row][col-1]=="O":

                            stack.append((row,col-1))
                            board[row][col-1]="T"
                        #right
                        if col<len(board[0])-1 and board[row][col+1]=="O":

                            stack.append((row,col+1))
                            board[row][col+1]="T"
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"
    
        