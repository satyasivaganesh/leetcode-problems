class Solution:
    def arrangeCoins(self, n: int) -> int:
        x=0
        c=0
        while 1:
            x+=1
            if n>=x:
                n=n-x
                c+=1
            else:
                break
        return c
            
        
