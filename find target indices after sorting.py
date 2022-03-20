class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        x=-1
        y=-1
        for i in range(len(nums)):
            if nums[i]==target:
                x=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                y=i
                break
        t=[]
        if x<0 and y<0:
            return t
        for i in range(x,y+1):
            t+=[i]
        return t
