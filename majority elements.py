class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        m=0
        if len(nums)==1:
            return nums[0]
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
                if dict[i]>m:
                    m=dict[i]
        
        for i in dict:
            if dict[i]==m:
                return i
