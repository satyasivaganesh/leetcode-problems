class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        t=nums.copy()
        nums.sort()
        x=0
        y=0
        print(t,nums)
        for i in range(len(nums)):
            if nums[i]!=t[i]:
                x=i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]!=t[j]:
                y=j
                break
        if(x==0 and y==0):
            return 0
        return (y-x)+1
        
