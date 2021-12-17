class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        l=0
        x=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    if int(matrix[i][j]):
                        x=2
                    matrix[i][j]=int(matrix[i][j])
                else:
                    if int(matrix[i][j]):
                        x=1
                        matrix[i][j]=min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))+1
                        if min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))+1>l:
                            l=min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1]))+1
        if x==1:
            return l*l
        if x==2:
            return 1
        return 0
                        
