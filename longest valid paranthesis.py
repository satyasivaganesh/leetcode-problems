class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=len(s)
        st=[]
        t=[0]*l
        m=0
        su=0
        for i in range(l):
            if s[i]=='(':
                st+=[i]
            else:
                if len(st):
                    t[st[-1]]=1
                    t[i]=1
                    st.pop()
        for j in range(l):
            if t[j]:
                su+=t[j]
                if j==l-1:
                    if su>m:
                        m=su
            else:
                if su>m:
                    m=su
                su=0
        print(t)
        return m
