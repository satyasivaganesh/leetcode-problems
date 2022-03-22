class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        t=['a']*n
        k=k-n
        for i in range(n-1,-1,-1):
            if k==0:
                break
            else:
                if k>=26:
                    t[i]=chr(97+25)
                    k-=25
                else:
                    y=1+k
                    t[i]=chr(96+y)
                    k=0
        return ''.join(t)
