      s=s.split(" ")
        dict={}
        t=[]
        x=0
        if len(pattern)!=len(s):
            return 0
        for i in pattern:
            if i not in dict:
                if s[x] not in t:
                    t+=[s[x]]
                else:
                    return 0
                dict[i]=s[x]
            else:
                if dict[i]!=s[x]:
                    return 0
            x+=1
        return 1
