class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        t=[]
        s=0
        for i in digits:
            s=s*10+i
        s+=1
        while s:
            r=s%10
            s=s//10
            t+=[r]
        t[:]=t[::-1]
        return t
