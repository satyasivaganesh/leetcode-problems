class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target<=i[-1]:
                l=0
                #if i[-1]==target:
                 #   return 1
                u=len(i)-1
                while(l<=u):
                    m=(l+u)//2
                    if i[m]==target:
                        return 1
                    if i[m]>target:
                        u=m-1
                    else:
                        l=m+1
        return 0
                
