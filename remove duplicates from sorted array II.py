class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t=[]
        for i in nums:
            if i not in t:
                t.append(i)
            else:
                if t.count(i)==1:
                    t.append(i)
        nums[:]=t[:]
                
