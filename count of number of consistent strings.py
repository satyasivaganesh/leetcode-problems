class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=list(allowed)
        c=0
        co=0
        for i in words:
            for j in range(len(i)):
                if i[j] in allowed:
                    c+=1
                if c==len(i):
                    co+=1
            c=0
                  
        return co
