class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        s=0
        t=[nums[0],nums[1]]
        d=nums[1]-nums[0]
        for i in range(2,len(nums)):
            if nums[i]-t[-1]==d:
                t+=[nums[i]]
            else:
                x=t[-1]
                if len(t)>=3:
                    l=len(t)
                    s+=(l-1)*(l-2)//2
                t=[x,nums[i]]
                d=nums[i]-x
        if len(t)>=3:
            l=len(t)
            s+=(l-1)*(l-2)//2
        return s
        
