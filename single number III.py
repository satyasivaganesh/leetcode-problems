class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        t=[]
        for i in nums:
            if i not in t:
                if(nums.count(i)==1):
                    t.append(i)
        return t
        
