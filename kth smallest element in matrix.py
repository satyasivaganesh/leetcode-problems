class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        c=0
        t=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c+=1
                t+=[matrix[i][j]]
        t.sort()
        return t[k-1]
