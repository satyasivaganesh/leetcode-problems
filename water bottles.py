class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        r=0
        x=nb
        while(nb>1):
            r=nb%ne
            nb=nb//ne
            if nb==0:
                break
            x+=nb
            nb=nb+r
        return x
