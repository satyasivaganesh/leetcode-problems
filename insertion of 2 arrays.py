class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t=[]
        dict1={}
        dict2={}
        l1=0
        l2=0
        for i in nums1:
            if i not in dict1:
                dict1[i]=1
                l1+=1
            else:
                dict1[i]+=1
                
        for j in nums2:
            if j not in dict2:
                dict2[j]=1
                l2+=1
            else:
                dict2[j]+=1
        if l1<=l2:
            for i in dict1:
                if i in dict2:
                    m=min(dict1[i],dict2[i])
                    t+=[i]*m
        else:
            for i in dict2:
                if i in dict1:
                    m=min(dict1[i],dict2[i])
                    t+=[i]*m
        return t
        
