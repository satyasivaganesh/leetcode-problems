class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        l=0
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                x=chr(ord(i)+32)
            elif ord(i)>=97 and ord(i)<=122:
                x=i
            elif ord(i)>=48 and ord(i)<=57:
                x=i
            else:
                x=''
            ans+=x
        i=0
        j=len(ans)-1
        while i<j:
            if ans[i]!=ans[j]:
                return 0
            i+=1
            j-=1
        return 1
