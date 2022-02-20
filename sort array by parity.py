class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev=[0]*(len(nums)//2)
        od=[0]*(len(nums)//2)
        e=0
        o=0
        for i in nums:
            if i%2==0:
                ev[e]=i
                e+=1
            else:
                od[o]=i
                o+=1
        t=[0]*len(nums)
        for i in range(len(nums)):
            if i%2==0:
                t[i]=ev[-1]
                ev.pop()
            else:
                t[i]=od[-1]
                od.pop()
        return t
