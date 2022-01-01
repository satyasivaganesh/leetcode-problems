class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        t=[]
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                t+=[[i+1,j+1]]
                break
            else:
                if numbers[i]+numbers[j]>target:
                    j-=1
                else:
                    i+=1
        return t[0]
