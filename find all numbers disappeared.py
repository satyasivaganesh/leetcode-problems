class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        t=[0]*(n+1)
        x=[]
        t[0]=1
        for i in nums:
            t[i]=1
        l=len(t)
        for i in range(l):
            if t[i]==0:
                x+=[i]
        return x
