class Solution:
    def maxProduct(self, words: List[str]) -> int:
        p=0
        for i in range(len(words)):
            dict={}
            for j in words[i]:
                if j not in dict:
                    dict[j]=1
                else:
                    dict[j]+=1
            for k in range(i+1,len(words)):
                ref=0
                for l in range(len(words[k])):
                    if words[k][l] in dict:
                        ref=1
                        break
                if ref==0:
                    ans=len(words[i])*len(words[k])
                    if ans>p:
                        p=ans
        return p
