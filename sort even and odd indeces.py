class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        ev=[nums[x] for x in range(0,len(nums),2)]
        od=[nums[y] for y in range(1,len(nums),2)]
        od.sort()
        ev.sort()
        od.reverse()
        t=[0]*len(nums)
        e=0
        o=0
        for i in range(len(nums)):
            if i%2==0:
                t[i]=ev[e]
                e+=1
            else:
                t[i]=od[o]
                o+=1
        return t
