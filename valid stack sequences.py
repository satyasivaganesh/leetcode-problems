class Solution:
    def validateStackSequences(self, pu: List[int], po: List[int]) -> bool:
        t=[]
        j=0
        for i in range(len(pu)):
            if pu[i]!=po[j]:
                t+=[pu[i]]
            else:
                j+=1
                while len(t) and t[-1]==po[j]:
                    t.pop()
                    j+=1
        if j==len(pu):
            return 1
        return 0
