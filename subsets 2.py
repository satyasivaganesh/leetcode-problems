class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        t=[]
        nums.sort()
        for i in range(pow(2,len(nums))):
            a=[]
            x=i
            ind=len(nums)-1
            while x:
                r=x&1
                x=x>>1
                if r:
                    a+=[nums[ind]]
                ind-=1
            t+=[a]
        ans=[]
        for i in t:
            if i not  in ans:
                ans+=[i]
        return ans
        
