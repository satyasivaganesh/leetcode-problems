class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        w=[]
        f=words[0]
        for l in f:
            if l not in w:
                w.append(l)
        t=[]
        for i in w:
            c=100
            for j in words:
                x=j.count(i)
                if x<c:
                    c=x
            for k in range(c):
                t.append(i)
        return t
            
        
