class Solution:
    def countPrimes(self, n: int) -> int:
        t=[1]*(n)
        c=0
        x=n
        for i in range(2,int(pow(n,0.5))+1):
            if t[i]:
                for j in range(i*i,n,i):
                    t[j]=0
        for k in range(2,n):
            if t[k]==1:
                c+=1
        if n<=2:
            return 0
        return c
