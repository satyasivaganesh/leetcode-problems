 def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        t=[]
        if target not in nums:
            return [-1,-1]
        else:
            for i in range(l):
                if nums[i]==target:
                    t+=[i]
                    break
            for i in range(1,l-i+1):
                if nums[-i]==target:
                    t+=[l-i]
                    break
            return t
