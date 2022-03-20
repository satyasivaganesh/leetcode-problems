class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        x=tops[0]
        y=bottoms[0]
        t=0
        b=0
        ref=0
        for i in range(len(tops)):
            if tops[i]==x and bottoms[i]!=x:
                b+=1
            elif bottoms[i]==x and tops[i]!=x:
                t+=1
            elif bottoms[i]==tops[i]==x:
                continue
            else:
                ref=1
                break
        if ref==0:
            return min(t,b)
        t=0
        b=0
        ref=0
        for i in range(len(tops)):
            if tops[i]==y and bottoms[i]!=y:
                b+=1
            elif bottoms[i]==y and tops[i]!=y:
                t+=1
            elif tops[i]==bottoms[i]==y:
                continue
            else:
                ref=1
                break
        if ref==0:
            return min(t,b)
        return -1
