class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        for i in range(l):
            if(i==0):
                if(nums[i]!=nums[i+1]):
                    break
            elif(i==l-1):
                if(nums[i]!=nums[i-1]):
                    break
            else:
                if(nums[i]!=nums[i-1] and nums[i]!=nums[i+1]):
                    break
        return nums[i] 
        
