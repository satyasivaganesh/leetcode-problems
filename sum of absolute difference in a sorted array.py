class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        li=nums.copy()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        t=[(nums[-1]-nums[0])-li[0]*(len(nums)-1)]
        for j in range(1,len(nums)):
            t+=[(li[j]*j-nums[j-1])+((nums[-1]-nums[j])-li[j]*(len(nums)-(j+1)))]
        return t
            
        
