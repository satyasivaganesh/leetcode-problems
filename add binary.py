class Solution:
    def addBinary(self, a: str, b: str) -> str:
        t=[]
        a=int(a)
        b=int(b)
        c=0
        s1=0
        s2=0
        while a:
            r=a%10
            a=a//10
            s1=s1+r*pow(2,c)
            c+=1
        c=0
        while b:
            r=b%10
            b=b//10
            s2=s2+r*pow(2,c)
            c+=1
        a=s1+s2
        s=''
        while a:
            r=a&1
            a=a>>1
            s+=str(r)
        if s=="":
            return "0"
        return s[::-1]
