class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        l=0
        if y>=x:
            while y:
                if x&1!=y&1:
                    l+=1
                x=x>>1
                y=y>>1
            return l
        else:
            while x:
                if x&1!=y&1:
                    l+=1
                x=x>>1
                y=y>>1
            return l
            
        
