class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        matrix=[[0]*n]*m
        #print(matrix)
        for i in range(m):
            for j in range(n):
                c=0
                if i and j:
                    if board[i-1][j-1]==1 or board[i-1][j-1]=='+':
                        c+=1
                if i:
                    if board[i-1][j]==1 or board[i-1][j]=='+':
                        c+=1
                if (i-1)>=0 and (j+1)<n:
                    if board[i-1][j+1]==1 or board[i-1][j+1]=='+':
                        c+=1
                if (j+1)<n:
                    if board[i][j+1]==1 or board[i][j+1]=='+' :
                        c+=1
                if (i+1)<m and (j+1)<n:
                    if board[i+1][j+1]==1 or board[i+1][j+1]=='+':
                        c+=1
                if (i+1)<m:
                    if board[i+1][j]==1 or board[i+1][j]=='+':
                        c+=1
                if (i+1)<m and (j-1)>=0:
                    if board[i+1][j-1]==1 or board[i+1][j-1]=='+':
                        c+=1
                if (j-1)>=0:
                    if board[i][j-1]==1 or board[i][j-1]=='+':
                        c+=1
                if board[i][j]==1 and c<2:
                    board[i][j]='+'
                elif board[i][j]==1 and c>3:
                    board[i][j]='+'
                elif board[i][j]==0 and c==3:
                    board[i][j]='*'
        for i in range(m):
            for j in range(n):
                if board[i][j]=='+':
                    board[i][j]=0
                elif board[i][j]=='*':
                    board[i][j]=1
               # '*' 0 to 1
               # '+' 1 to 0
