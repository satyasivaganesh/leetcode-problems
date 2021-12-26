class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        t=[]
        y=[]
        dict={}
        ans=[]
        for i in range(len(points)):
            x=math.sqrt(pow(points[i][0],2)+pow(points[i][1],2))
            dict[i]=x
        dict={k: v for k, v in sorted(dict.items(), key=lambda v: v[1])}
        print(dict)
        l=0
        for j in dict:
            l+=1
            if l>k:
                break
            else:
                ans+=[points[j]]
        return ans
        
