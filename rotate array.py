class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=len(nums)
        x=k%l
        nums[:]=nums[l-x::]+nums[:l-x:]
        
            
        
