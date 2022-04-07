class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        c=''
        y=arr[0]
        n=len(arr)
        ref=0
        x=len(arr[0])
        for i in range(x):
            st=arr[0][i]
            for j in range(1,n):
                if i==len(arr[j]) or arr[j][i]!=st:
                    ref=1
                    break
            if ref==0:
                c+=st
            else:
                break
        if c=='':
            return ''
        return c
