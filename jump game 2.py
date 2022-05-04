class Solution:
    def jump(self, nums: List[int]) -> int:
        t=[0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]!=0:
                if (i+nums[i])>=(len(nums)-1):
                    t[i]+=1
                else:
                    m=0
                    ref=0
                    for j in range(i+1,i+nums[i]+1):
                        if(t[j]!=0):
                            if m==0 and ref==0:
                                m=t[j]
                                ref=1
                            elif t[j]<m:
                                m=t[j]
                    if(m==0):
                        t[i]=0
                    else:
                        t[i]+=(m+1)
                #print(t)
        #print(t)
        return t[0]
