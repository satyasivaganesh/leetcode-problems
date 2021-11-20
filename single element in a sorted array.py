class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            c=nums.count(i)
            if c==1:
                return i
        
