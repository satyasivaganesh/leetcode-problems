class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                return 1
        return 0