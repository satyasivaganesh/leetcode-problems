class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        x=nums[0]
        if len(nums)==1:
            return 0
        for i in range(1,len(nums)):
            if nums[i]<x:
                return i-1
            elif i==len(nums)-1:
                return i
            x=nums[i]
            
