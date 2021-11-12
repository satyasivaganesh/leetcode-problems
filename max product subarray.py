class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        ma=[nums[0]]
        mi=[nums[0]]
        ans=nums[0]
        for i in range(1,l):
            x=max(nums[i],nums[i]*ma[-1],nums[i]*mi[-1])
            y=min(nums[i],nums[i]*ma[-1],nums[i]*mi[-1])
            ma+=[x]
            mi+=[y]
            if ans<ma[-1]:
                ans=ma[-1]
        return ans
      
      
   //or
  class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        ma=nums[0]
        mi=nums[0]
        ans=nums[0]
        for i in range(1,l):
            x=max(nums[i],nums[i]*ma,nums[i]*mi)
            y=min(nums[i],nums[i]*ma,nums[i]*mi)
            ma=x
            mi=y
            if ans<ma:
                ans=ma
        return ans
