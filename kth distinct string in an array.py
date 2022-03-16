class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict={}
        for i in arr:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        c=0
        for i in dict:
            if dict[i]==1:
                c+=1
                if c==k:
                    return i
        if c<k:
            return ""
