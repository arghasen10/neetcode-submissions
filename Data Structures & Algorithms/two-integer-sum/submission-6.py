class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}
        vals = []
        for i, e in enumerate(nums):
            if e in reminder:
                vals = [reminder[e], i]
                break
            else:
                reminder[target-e] = i    
        return vals