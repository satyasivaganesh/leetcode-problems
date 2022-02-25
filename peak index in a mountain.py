class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        x=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<x:
                return i-1
            x=arr[i]
            
        
