class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=len(nums)
        if target in nums:
            return nums.index(target)
        for i in range(l):
            if nums[i]>target:
                return i
        else:
            return l
        
