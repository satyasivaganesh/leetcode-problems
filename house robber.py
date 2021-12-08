class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        #if len(nums)==3:
            #return max(nums[0],nums[1])
        t=[0]*len(nums)
        t[-1]=nums[-1]
        t[-2]=nums[-2]
        for i in range(3,len(nums)+1):
            x=nums[-i]+t[-1]
            for j in range(1,i-1):
                y=t[-j]+nums[-i]
                if y>=x:
                    x=y
            t[-i]=x
        return max(t[0],t[1])
                
