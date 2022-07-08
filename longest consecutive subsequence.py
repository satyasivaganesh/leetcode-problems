class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        num=[]
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
                num+=[i]
            else:
                dict[i]+=1
        m=1
        c=1
        for i in range(1,len(num)):
            if num[i]-num[i-1]==1:
                c+=1
                    
            
            
            else:
                if c>m:
                    m=c
                c=1
            print(c,end=' ')
        if c>m:
            return c
        return m
