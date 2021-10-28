    def threeSum(self, nums: List[int]) -> List[List[int]]:
        t=[]
        l=len(nums)
        nums.sort()
        for i in range(l):
            j=i+1
            k=l-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    x=[nums[i],nums[j],nums[k]]
                    if x not in t:
                        t.append(x)
                    k-=1
                    j+=1
                elif s>0:
                    k-=1
                else:
                    j+=1
        return t
