class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        a=1
        z=1
        y=0
        if k==1:
            return 1
        if k%2==0:
            return -1
        else:
            while z<=k:
                if a%k==0:
                    y=1
                    break
                a=a*10+1
                z+=1
            if y==1:
                return z
            return -1
        
