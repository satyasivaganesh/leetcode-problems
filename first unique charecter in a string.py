for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        else:
            return -1
