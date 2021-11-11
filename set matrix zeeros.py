class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=[]
        c=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    r+=[i]
                    c+=[j]
        for k in range(len(r)):
            for i in range(m):
                for j in range(n):
                    if i==r[k] or j==c[k]:
                        matrix[i][j]=0
        return matrix
                
