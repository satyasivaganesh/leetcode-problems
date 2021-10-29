class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)
        if l==1:
            return 1
        x=[0]*l
        j=l-1
        i=j-1
        while 1:
            if i+nums[i]>=j:
                x[j]=1
                for k in range(i,j):
                    x[k]+=1
                    print(k,j)
                j=i
                i=j-1
            else:
                i-=1
            if i<0:
                break
        print(x)
        if 0 not in x:
            return 1
        return 0
