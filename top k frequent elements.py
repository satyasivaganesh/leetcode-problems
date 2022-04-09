class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        t=[]
        l=0
        for i in nums:
            if i not in dict:
                t+=[i]
                l+=1
                dict[i]=1
            else:
                dict[i]+=1
        ans=[t[0]]
        le=1
        for i in range(1,l):
            ref=0
            for j in range(le):
                if dict[t[i]]<=dict[ans[j]]:
                    ans.insert(j,t[i])
                    le+=1
                    ref=1
                    break
            if ref==0:
                ans+=[t[i]]
                le+=1
        return ans[l-k::]
