class Solution:
    def maxPower(self, s: str) -> int:
        x=1
        t=[]
        l=len(s)
        if l==1:
            return 1
        if l==2 and s[1]==s[0]:
            return 2

        for i in range(1,l):
            if s[i]==s[i-1]:
                x+=1
                if l-1==i:
                    t+=[x]
            else:
                t+=[x]
                x=1
        return max(t)
            
