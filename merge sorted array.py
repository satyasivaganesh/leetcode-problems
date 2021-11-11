class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        t=[]
        t[:]=nums1[:m]
        if n!=0:
            t.extend(nums2)
        t.sort()
        nums1[:]=t[:]
        
        
