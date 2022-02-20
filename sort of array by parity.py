class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ev=[]
        od=[]
        for i in nums:
            if i%2==0:
                ev+=[i]
            else:
                od+=[i]
        return ev+od
        
