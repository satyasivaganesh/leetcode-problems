class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=len(needle)
        for i in range(len(haystack)-x+1):
            y=haystack[i:i+x]
            if y==needle:
                return i
        else:
            return -1
            
