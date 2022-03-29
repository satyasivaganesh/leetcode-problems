class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        s=0
        print(arr)
        for i in range(2,len(arr),2):
            x=0
            s+=arr[i]
            for j in range(i+1,len(arr)):
                s+=(arr[j]-arr[x])
                x+=1
        return s+arr[-1]
            
