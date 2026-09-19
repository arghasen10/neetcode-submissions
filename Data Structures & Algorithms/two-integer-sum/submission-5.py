class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = {}
        for i, e in enumerate(nums):
            if (target-e) in elems:
                return [elems[(target-e)], i]
            else:
                elems[e] = i

        
