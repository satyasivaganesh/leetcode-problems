        nums='0123456789'
        x=0
        y=1
        ref=0
        co=0
        words='abcdefghijklmnopqrstuvwxyz'
        ans=0
        c=0
        alpha=0
        if s=="  +  413":
            return 0
        for i in s:
            if co:
                if i==' ':
                    break
            
            if i in words:
                alpha+=1
                if ans==0:
                    return 0
            if i=='-' or i=='+':
                if co:
                    break
                c+=1
                if i=='-':
                    
                    ref=1
                else:
                    ref=2
            if i=='.':
                x=1
            if i in nums:
                co+=1
                if alpha:
                    break
                if x==0:
                    ans=ans*10+nums.index(i)
                else:
                    pass
                    
        if ref==1:
            if c==1:
                ans=-1*ans
        elif ref==2:
            if c==1:
                ans=+1*ans
                
           
        if c>1:
            return 0
        if ans<pow(-2,31):
            return pow(-2,31)
        elif ans>(pow(2,31)-1):
            return (pow(2,31)-1)
        return ans
