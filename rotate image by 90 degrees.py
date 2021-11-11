class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        t=[]
        for i in range(0,n):
            for j in range(0,n):
                t+=[matrix[n-1-j][i]]
        l=0
        for i in range(n):
            for j in range(n):
                matrix[i][j]=t[l]
                l+=1
        
