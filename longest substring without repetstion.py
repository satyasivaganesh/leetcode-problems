class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            ref=0
            dict={}
            l=0
            for j in range(i,len(s)):
                if s[j] not in dict:
                    dict[s[j]]=1
                    l+=1
                else:
                    ref=1
                    if l>m:
                        m=l
                    break
            if ref==0:
                if l>m:
                    m=l
                break
        return m
        
