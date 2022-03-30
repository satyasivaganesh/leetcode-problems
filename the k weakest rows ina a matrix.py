class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        t=[sum(mat[0])]
        ind=[0]
        l=1
        for i in range(1,len(mat)):
            s=sum(mat[i])
            for j in range(l):
                if s<t[j]:
                    t.insert(j,s)
                    ind.insert(j,i)
                    l+=1
                    break
            else:
                t+=[s]
                ind+=[i]
                l+=1
        #print(t)
        return ind[:k:]
            
