class Solution:
    def brokenCalc(self, stv: int, tar: int) -> int:
        c=0
        while stv<tar:
            if tar%2==0:
                tar=tar//2
                c+=1
            else:
                tar+=1
                c+=1
        if tar==stv:
            return c
        else:
            return c+stv-tar
            
