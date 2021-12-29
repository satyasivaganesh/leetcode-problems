class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        t=[]
        s=0
        for i in num:
            s=s*10+i
        s=s+k
        y=s
        while s:
            r=s%10
            s=s//10
            t+=[r]
        if y==0:
            return [0]
        t[:]=t[::-1]
        return t
