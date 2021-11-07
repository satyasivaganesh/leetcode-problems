class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t=[]
        for i in nums:
            if i!=val:
                t.append(i)
        nums[:]=t[:]
        
