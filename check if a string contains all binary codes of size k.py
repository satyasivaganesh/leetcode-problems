class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dict={}
        for i in range(len(s)-k+1):
            x=s[i:i+k]
            if x not in dict:
                dict[x]=1
        for i in range(pow(2,k)):
    
            z=i
            ans=""
            while(z):
                r=z&1
                if(r):
                    ans='1'+ans
                else:
                    ans='0'+ans
                z=z>>1
            print(ans,end=" ")
            if len(ans)<k:
                ans="0"*(k-len(ans))+ans
            print(ans)
            if ans not in dict:
                return 0
        return 1
