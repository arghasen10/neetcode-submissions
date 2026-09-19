class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elemts = {}
        for num in nums:
            if num in elemts:
                elemts[num] +=1
            else:
                elemts[num] =1
        for k,v in elemts.items():
            if v >1:
                return True
        return False