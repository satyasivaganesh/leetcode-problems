class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        t=[]
        for i in range(left,right+1):
            x=str(i)
            ref=0
            for j in x:
                if int(j)==0:
                    ref=1
                    continue
                if i%int(j)!=0:
                    ref=1
                    break
            if ref==0:
                t+=[i]
        return t
                        
            
        
