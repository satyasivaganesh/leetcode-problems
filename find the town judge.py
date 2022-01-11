        t=[]
        dict={}
        if trust==[]:
            if n==1:
                return 1
            return -1
        for i in trust:
            if i[0] not in dict:
                dict[i[0]]=[i[1]]
            else:
                dict[i[0]]+=[i[1]]
            if i[0] not in t:
                t+=[i[0]]
        co=[]
        for j in trust:
            if j[1] not in t:
                if j[1] not in co:
                    co+=[j[1]]
        if len(co)>1:
            return -1
        if len(co)==0:
            return -1
                
        ans=co[0]
        refe=0
        for k in dict:
            if ans not in dict[k]:
                refe=1
                break
        if refe==0:
            return ans
        return -1
