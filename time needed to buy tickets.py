class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        t=0
        s=0
        for i in range(len(tickets)):
            if i>k and tickets[i]>=tickets[k]:
                t+=1
            if tickets[i]<tickets[k]:
                s+=i
            else:
                c+=1
        return s+c*tickets[k]-t
            
        
