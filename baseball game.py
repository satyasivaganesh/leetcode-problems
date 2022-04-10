class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=[]
        s=0
        num='-0123456789'
        for i in ops:
            if i[0] in num:
                st+=[int(i)]
                s+=int(i)
            elif i=='C':
                x=st.pop()
                s-=x
            elif i=='+':
                st+=[st[-1]+st[-2]]
                s+=st[-1]
            else:
                st+=[st[-1]*2]
                s+=st[-1]
        return s
