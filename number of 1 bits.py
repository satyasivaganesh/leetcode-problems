class Solution:
    def hammingWeight(self, n: int) -> int:
        l=0
        while n:
            if n&1!=0:
                l+=1
            n=n>>1
        return l
        
