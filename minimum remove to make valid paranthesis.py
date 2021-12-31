class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        t=[]
        ans=[]
        x=[]
        s=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                t+=[i]
            elif s[i]==')':
                if len(t)==0:
                    x+=[i]
                else:
                    t.pop()
        if len(t):
            for j in t:
                x+=[j]
        for i in range(len(s)):
            if i not in x:
                ans+=[s[i]]
        return ''.join(ans)
        
