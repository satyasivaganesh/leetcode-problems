class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        u=max(piles)
        while(l<=u):
            m=(l+u)//2
            s=0
            for i in piles:
                if(i%m==0):
                    s+=i//m
                else:
                    s+=(i//m)+1
            if s>h:
                l=m+1
            else:
                u=m-1
        return l
                    
