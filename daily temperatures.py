class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        st1=[temperatures[-1]]
        st2=[l-1]
        ans=[0]
        for i in range(2,l+1):
            if temperatures[-i]<st1[-1]:
                ans+=[st2[-1]-l+i]
                st1+=[temperatures[-i]]
                st2+=[l-i]
            else:
                while temperatures[-i]>=st1[-1]:
                    st1.pop()
                    st2.pop()
                    if len(st1)==0:
                        ans+=[0]
                        break
                if len(st1):
                    ans+=[st2[-1]-l+i] 
                st1+=[temperatures[-i]]
                st2+=[l-i]
        ans.reverse()
        return ans 
        
