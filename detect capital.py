class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap=0
        small=0
        l=len(word)
        for i in word:
            if ord(i)>=65 and ord(i)<=90:
                cap+=1
            else:
                small+=1
        if cap==l or small==l:
            return 1
        elif cap==1:
            if ord(word[0]) in range(65,91):
                return 1

        return 0
