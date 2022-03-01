class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        t=[]
        if len(nums)==0:
            return []
        st=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]-st[-1]<=1:
                st+=[nums[i]]
                
            else:
                if len(st)==1:
                    t+=[str(st[-1])]
                    st.pop()
                    st+=[nums[i]]
                else:
                    y=st[-1]
                    x=st[0]
                    while len(st):
                        st.pop()
                    t+=[str(x)+'->'+str(y)]
                    st+=[nums[i]]
        if len(st)==1:
            t+=[str(st[-1])]
            st.pop()
        elif len(st)>1:
            y=st[-1]
            x=st[0]
            t+=[str(x)+'->'+str(y)]
        
        return t
