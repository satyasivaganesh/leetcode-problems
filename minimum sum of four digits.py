class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        x=num[:2:]
        y=num[2::]
        s=min(int(x[::-1]),int(x))+min(int(y[::-1]),int(y))
        z=num[0]+num[-1]
        a=num[1]+num[2]
        return min(s,min(int(z),int(z[::-1]))+min(int(a),int(a[::-1])))
        
        
